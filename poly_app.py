################################################################################
# STANDARD LIB IMPORTS
import sys, os, time
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
from pawpaw import WebApp, Router, route, Template, LazyTemplate

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
try:
    import board, nativeio #CircuitPython specific
    PINS[0]  = board.GPIO0
    PINS[2]  = board.GPIO2
    PINS[4]  = board.GPIO4
    PINS[5]  = board.GPIO5
    PINS[12] = board.GPIO12
    PINS[13] = board.GPIO13
    PINS[14] = board.GPIO14
    PINS[15] = board.GPIO15
    #set all pins to input, safest state
    for pin_num, board_pin in PINS.items():
        with nativeio.DigitalInOut(board_pin) as d_in:
            d_in.switch_to_input()
#    with nativeio.DigitalInOut(PINS[2]) as d_out:
#            d_out.switch_to_output()
#            d_out.value =
except ImportError:
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
    
ht_sensor = AM2315()
ht_sensor.init()

################################################################################
# APPLICATION CODE
#-------------------------------------------------------------------------------
@Router
class PolyServer(WebApp):
    @route("/", methods=['GET'])
    def index(self, context):
        global DEBUG
        if DEBUG:
            print("INSIDE ROUTE HANDLER name='%s' " % ('index'))
            try:
                from micropython import mem_info
                mem_info()
            except ImportError:
                pass
                
        #open the template files
        def gen_index_tmp(chunksize = 64):
            with open("html/index.html", 'r') as f:
                while True:
                    chunk = f.read(chunksize)
                    if not chunk:
                        return
                    yield chunk
        index_tmp = gen_index_tmp()
        #finally render the view
        context.render_template(index_tmp)
        
    @route("/test", methods=['GET'])
    def index(self, context):
        global DEBUG
        if DEBUG:
            print("INSIDE ROUTE HANDLER name='%s' " % ('index'))
            try:
                from micropython import mem_info
                mem_info()
            except ImportError:
                pass
        tmp = LazyTemplate.from_file("html/test.html")
        #finally render the view
        context.render_template(tmp)
    
    @route("/pins", methods=['GET','PUT'])
    def pins(self, context):
        global DEBUG
        if DEBUG:
            print("INSIDE ROUTE HANDLER name='%s' " % ('pins'))
            print("\trequest.args: %r" % (context.request.args,))
            try:
                from micropython import mem_info
                mem_info()
            except ImportError:
                pass
        pin_num  = int(context.request.args['pin_num'])
        pin_type = context.request.args['pin_type']
        pin_value = None
        pin = PINS[pin_num]
        if context.request.method == 'PUT':
            pin_value = json.loads(context.request.args['pin_value']) #converts 'false' to False, 'true' to True
            if pin_type == "digital_out":
                if DEBUG:
                    print("SETTING pin_type = 'digital_out' to pin_value = %s" % pin_value)
                try:
                    #CircuitPython specific
                    import nativeio
                    if DEBUG:
                        print("USING HARDWARE INTERFACE nativeio.DigitalInOut")
                    with nativeio.DigitalInOut(PINS[pin_num]) as d_out:
                        d_out.switch_to_output()
                        d_out.value = pin_value
                except ImportError:
                    #works in micropython and PC
                    if DEBUG:
                        print("USING HARDWARE INTERFACE machine.Pin")
                    PINS[pin_num] = pin = machine.Pin(pin_num,machine.Pin.OUT)
                    pin.value(pin_value)
        elif context.request.method == 'GET':
            if DEBUG:
                print("GETTING pin_type = '%s'" % pin_type)
            try:
                #CircuitPython specific
                import nativeio
                if DEBUG:
                    print("USING HARDWARE INTERFACE nativeio.DigitalInOut")
                with nativeio.DigitalInOut(PINS[pin_num]) as d:
                    pin_value = d.value
            except ImportError:
                #works in micropython and PC
                if DEBUG:
                    print("USING HARDWARE INTERFACE machine.Pin")
                pin = PINS[pin_num]
                pin_value = pin.value()
        resp = {'pin_num': pin_num, 'pin_value': pin_value}
        context.send_json_response(resp)
        
    @route("/am2315", methods=['GET'])
    def am2315(self, context):
        global DEBUG
        if DEBUG:
            print("INSIDE ROUTE HANDLER name='%s' " % ('am2315'))
            print("\trequest.args: %r" % (context.request.args,))
            try:
                from micropython import mem_info
                mem_info()
            except ImportError:
                pass
        d = {}
        #acquire a humidity and temperature sample
        ht_sensor.get_data(d)  #adds fields 'humid', 'temp'
        print("SENDING DATA AS JSON: %r" % (d,))
        context.send_json_response(d)
        
################################################################################
# MAIN
#-------------------------------------------------------------------------------
#if __name__ == "__main__":
#---------------------------------------------------------------------------
# Create application instance binding to localhost on port 9999
app = PolyServer(server_addr = SERVER_ADDR,
                 server_port = SERVER_PORT,
               )
#if DEBUG:
#    print("APP HANDLER REGISTRY: %s" % app.handler_registry)
    #h = app.handler_registry['GET /']
    #h({})
# Activate the server; this will keep running until you
# interrupt the program with Ctrl-C
app.serve_forever()
