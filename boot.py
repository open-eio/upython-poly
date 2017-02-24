# This file is executed on every boot (including wake-boot from deepsleep)
import esp
if hasattr(esp,'osdebug'):  #not yet available on ESP32 port
    esp.osdebug(None)
import gc
import network #needed for sockets on ESP32
try:
    import webrepl
    webrepl.start()
except ImportError:
    pass
    
gc.collect()
