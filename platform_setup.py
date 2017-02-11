import sys, os, time

try:
    import json
except ImportError:
    import ujson as json #micropython specific
    
################################################################################
# CONFIGURATION
#-------------------------------------------------------------------------------
#read the SECRET configuration file, NOTE this contains PRIVATE keys and 
#should never be posted online
CONFIG_FILENAME = "SECRET_CONFIG.json"

config = {}
if CONFIG_FILENAME in os.listdir():
    config = json.load(open(CONFIG_FILENAME,'r'))

#load configuration for this module
app_cfg = config.get('poly_app', {})

DEBUG   = app_cfg.get('debug', 0)

SERVER_ADDR = app_cfg.get('server_addr')
SERVER_PORT = app_cfg.get('server_port')

################################################################################
# PLATFORM SPECIFIC SETUP
#-------------------------------------------------------------------------------
PLATFORM = sys.platform
if DEBUG:
    print("DETECTED PLATFORM: %s" % PLATFORM)
# ------------------------------------------------------------------------------
# ESP8266
if PLATFORM == 'esp8266':
    import network_setup
    if DEBUG:
        print("RUNNING network_setup.do_connect:")
    sta_if, ap_if = network_setup.do_connect(**config['network_setup'])
    time.sleep(1.0)
    if SERVER_ADDR is None:
        #get DHCP address
        info = sta_if.ifconfig()
        SERVER_ADDR = info[0]
        if DEBUG:
            print("DEFAULTING SERVER_ADDR to '%s'" % SERVER_ADDR)
    if SERVER_PORT is None:
        SERVER_PORT = 80            #default HTTP port
        if DEBUG:
            print("DEFAULTING SERVER_PORT to '%s'" % SERVER_PORT)
    # Network/Services setup
   
# ------------------------------------------------------------------------------
# DEFAULT PLATFORM
else:
    if SERVER_ADDR is None:
        SERVER_ADDR = "0.0.0.0" #default to localhost
        if DEBUG:
            print("DEFAULTING SERVER_ADDR to '%s'" % SERVER_ADDR)
    if SERVER_PORT is None:
        SERVER_PORT = 8080      #alternate HTTP port
        if DEBUG:
            print("DEFAULTING SERVER_PORT to '%s'" % SERVER_PORT)
