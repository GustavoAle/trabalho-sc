import time

lastpoint = 0

def time_elapsed(function):
    start = time.ticks_us()
    function()
    end = time.ticks_us()
    return end-start

def equilibrar(setpoint,mpu,stepr):
    curpoint = mpu.get_values2()
    lastpoint = curpoint

    while True:
        try:
            curpoint = mpu.get_values2()
        except:
            print("Read error")
            continue
        if abs(curpoint) > 30:
            continue

        if (curpoint > lastpoint*1.5) or (curpoint < lastpoint*0.5):
            print("Out of reading")
            continue

        if stepr.__curstep__ > stepr.__maxstep__:
            stepr.step2(-20)
        if stepr.__curstep__ < stepr.__minstep__:
            stepr.step2(20)

        ang = (curpoint-setpoint)
        stepr.step2(ang/0.6)

        lastpoint = curpoint
