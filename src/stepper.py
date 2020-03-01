from machine import Pin
import exceptions
import time

class Stepper():
    #init class
    def __init__(self, step=15, dir=13, pulsedelay = 10):
        self.__steppin__ = Pin(step)
        self.__dirpin__ = Pin(dir)
        self.__pulsedelay__ = pulsedelay
        self.__curdir__ = 0
        self.__dirpin__.off()
        self.__steppin__.on()

    def dir(newdir = None):
        if newdir == None:
            return self.__curdir__
        self.__curdir__ = (newdir and 1)
        return (newdir and 1)

    def __pulse__():
        self.__steppin__.off()
        time.sleep_ms(self.__pulsedelay__)
        self.__steppin__.on()


    def step(nsteps = 1):
        if nsteps >= 50:
            raise OverStep()

        for i in range(0,nsteps):
            self.__pulse__()
