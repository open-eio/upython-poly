import machine, time
from machine import Timer

LOOP_PY_TIMEOUT_MS = 5000

def timeout_callback(t):
    machine.reset()

timer = Timer(0)
timer.init(period=LOOP_PY_TIMEOUT_MS, mode=Timer.ONE_SHOT, callback=timeout_callback)

cnt = 0
while True:
    cnt += 1
    print("%d... duh" % cnt)
    time.sleep(1.0)
