DEBUG = False
#DEBUG = True

CMD_NULL_REQUEST       = bytes(())
CMD_REQUEST_HUMID_TEMP = bytes((0x03,0x00,0x04))


class AM2315(object):
    """dummy driver
    """
    def __init__(self, scl = 5, sda = 4, i2c_addr = 0x5C):
        self.active = False
        
    def init(self):
        self.active = True
            
    def get_data(self, d = None):
        if d is None:
            d = {}
        if not self.active:
            return d
        else:
            #some fake values
            d['humid'] = 75.0
            d['temp']  = 25.0
            return d
            
################################################################################
# TEST CODE
################################################################################
if __name__ == "__main__":
    ht_sensor = AM2315()
    ht_sensor.init()
    d = {}
    ht_sensor.get_data(d)
    print(d)
