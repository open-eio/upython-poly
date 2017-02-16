################################################################################
# STANDARD LIB IMPORTS
import sys, os, time, gc
try:
    from collections import OrderedDict
except ImportError:
    from ucollections import OrderedDict #micropython specific
    
try:
    import json
except ImportError:
    import ujson as json #micropython specific

#-------------------------------------------------------------------------------
# PAWPAW PACKAGE IMPORTS
from pawpaw import WebApp, Router, route, Template, LazyTemplate, AutoTreeFormat
from pawpaw import auto_tree_format
#-------------------------------------------------------------------------------
# LOCAL IMPORTS


################################################################################
# PLATFORM SPECIFIC SETUP
#-------------------------------------------------------------------------------

import platform_setup
SERVER_ADDR = platform_setup.SERVER_ADDR
SERVER_PORT = platform_setup.SERVER_PORT
DEBUG       = platform_setup.DEBUG

if DEBUG:
    print("INSIDE MODULE name='%s' " % ('poly_app',))
    try:
        from micropython import mem_info #micropython specific
        mem_info()
    except ImportError:
        pass
################################################################################
# HARDWARE INTERFACES
#-------------------------------------------------------------------------------
PINS = OrderedDict()
#try:
#    import board, nativeio #CircuitPython specific
#    PINS[0]  = board.GPIO0
#    PINS[2]  = board.GPIO2
#    #PINS[4]  = board.GPIO4 #FIXME using this pin gives occasional 
#                            #"ValueError: Pin GPIO4 in use"
#    PINS[5]  = board.GPIO5
#    PINS[12] = board.GPIO12
#    PINS[13] = board.GPIO13
#    PINS[14] = board.GPIO14
#    PINS[15] = board.GPIO15
#    #set all pins to input, safest state
#    for pin_num, board_pin in PINS.items():
#        with nativeio.DigitalInOut(board_pin) as d_in:
#            d_in.switch_to_input()
#    with nativeio.DigitalInOut(PINS[2]) as d_out:
#            d_out.switch_to_output()
#            d_out.value =
#except ImportError:
try:
    import machine #micropython specific
except ImportError:
    import mock_machine as machine #a substitute for PC testing
        
pin_numbers = (0, 2, 4, 5, 12, 13, 14, 15)
PINS = OrderedDict((i,machine.Pin(i, machine.Pin.IN)) for i in pin_numbers)
    
#configure humidity/temperature sensor interface
try:
    from am2315 import AM2315
except ImportError:
    from mock_am2315 import AM2315
    
try:
    from micropython import mem_info
except ImportError:
    mem_info = lambda: None
    
ht_sensor = AM2315()
ht_sensor.init()


################################################################################
# APPLICATION CODE
#-------------------------------------------------------------------------------
@Router
class PolyServer(WebApp):
    @route("/", methods=['GET'])
    def index(self, context):
        context.send_file("html/index.html")
        
    @route("/test", methods=['GET'])
    def test(self, context):
        context.send_file("html/test.html")
        
    @route("/config", methods=['GET','POST'])
    def config(self, context):
        config_filename = "SECRET_CONFIG.json"
        comment = ""
                
        if context.request.method == 'POST':
            body = context.request.body
            form = auto_tree_format.parse_form_url(body)
            comment = "'%s' has been updated" % config_filename
            with open(config_filename,'w') as f:
                f.write(json.dumps(form))
            gc.collect()
            
        ATF = AutoTreeFormat.from_json_file(config_filename)
        gen_form = ATF.gen_html_form()
        tmp = LazyTemplate.from_file("html/config_form.html", endline = "", rstrip_lines = False)
        tmp.format(form_content = gen_form, comment = comment)
        context.render_template(tmp)
        
    @route("/logs/PolyServer.yaml", methods=['GET','DELETE'])
    def logs(self, context):
        if context.request.method == 'GET':
            context.send_file("logs/PolyServer.yaml")
        elif context.request.method == 'DELETE':
            os.remove("logs/PolyServer.yaml")
            open("logs/PolyServer.yaml",'w').close()
            context.send_json({})
        
    @route("/exc", methods=['PUT'])
    def exc(self, context):
        context.send_json({})
        raise Exception("this is a test")
    
    @route("/pins", methods=['GET','PUT'])
    def pins(self, context):
        pin_num  = int(context.request.args['pin_num'][0])
        pin_type = context.request.args['pin_type'][0]
        pin_value = None
        pin = PINS[pin_num]
        if context.request.method == 'PUT':
            pin_value = json.loads(context.request.args['pin_value'][0]) #converts to int
            pin_value = bool(pin_value)
            if pin_type == "digital_out":
                PINS[pin_num] = pin = machine.Pin(pin_num,machine.Pin.OUT)
                pin.value(pin_value)
        elif context.request.method == 'GET':
            #works in micropython and PC
            pin = PINS[pin_num]
            pin_value = pin.value()
        pin_value = 1 if pin_value else 0
        resp = {'pin_num': pin_num, 'pin_value': pin_value}
        context.send_json(resp)
        
    @route("/am2315", methods=['GET'])
    def am2315(self, context):
        d = {}
        #acquire a humidity and temperature sample
        ht_sensor.get_data(d)  #adds fields 'humid', 'temp'
        context.send_json(d)
        
    def run(self, control_loop_period = 10.0):
        import loop
        t0 = time.monotonic()
        t_last_ctrl_loop = time.monotonic()
        while True:
            #handle any waiting requests
            has_timedout = self.serve_once()
            t_now = time.monotonic()
            if (t_now - t_last_ctrl_loop) > control_loop_period:
                print("RUNNING CONTROL LOOP")
                loop.run(t_now)
                t_last_ctrl_loop = t_now
        
################################################################################
# MAIN
#-------------------------------------------------------------------------------
#if __name__ == "__main__":
#---------------------------------------------------------------------------
# Create application instance binding to localhost on port 9999
time.sleep(2.0)
gc.collect()

app = PolyServer(server_addr = SERVER_ADDR,
                 server_port = SERVER_PORT,
                 socket_timeout = 1.0,
               )
#if DEBUG:
#    print("APP HANDLER REGISTRY: %s" % app.handler_registry)
    #h = app.handler_registry['GET /']
    #h({})
# Activate the server; this will keep running until you
# interrupt the program with Ctrl-C
app.run()
