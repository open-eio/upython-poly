#configure humidity/temperature sensor interface
try:
    from am2315 import AM2315
except ImportError:
    from mock_am2315 import AM2315
    
import time
    
ht_sensor = AM2315()
ht_sensor.init()


def run(t_now):
    d = {}
    #acquire a humidity and temperature sample
    ht_sensor.get_data(d)  #adds fields 'humid', 'temp'
    print("loop.run:\n\tt_now: %f\n\tDATA: %r" % (t_now,d))
    time.sleep(10)
