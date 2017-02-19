import machine, time
from machine import Timer

TIMEOUT_MS = 5000 #soft-reset will happen around 5 sec

def timeout_callback(t):
    try:
        raise Exception("Timeout!")
    finally:
        machine.reset()  #FIXME, gentler way to break out?


def trial_function():
    cnt = 0
    while True:
        print("%d..." % cnt)
        time.sleep(1.0)
        cnt += 1
        
try:
    timer = Timer(0)
    timer.init(period=TIMEOUT_MS, mode=Timer.ONE_SHOT, callback=timeout_callback)
    trial_function()
    timer.deinit()
except Exception as exc:
    print("Caught exc: %s" % exc)
