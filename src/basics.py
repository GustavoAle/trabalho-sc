import time

def time_elapsed(function):
    start = time.ticks_us()
    function()
    end = time.ticks_us()
    return end-start