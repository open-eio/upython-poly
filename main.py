import time
import machine
from micropython import mem_info

print("main.py running:")
mem_info()

msg = None
try:
    from machine import UART #not yet available on ESP32 port!
    print("Waiting for connection on UART 0...",end="")
    time.sleep(1.0)

    uart = machine.UART(0, 115200)# init with given baudrate

    uart.init(115200, bits=8, parity=None, stop=1, timeout=1000) # init with given parameters
    msg = uart.read(1)
except ImportError:
    pass

if msg is None:
    print("timed out.")
    print("Loading poly_app")
    import poly_app
else:
    print(msg)
    print("Rerouting to REPL")
