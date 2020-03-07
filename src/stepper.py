from machine import Pin
import exceptions
import time

class Stepper():
    #init class
    def __init__(self, step=15, dir=13, pulsedelay = 10000):
        self.__steppin__ = Pin(step,Pin.OUT)
        self.__dirpin__ = Pin(dir,Pin.OUT)
        self.__pulsedelay__ = pulsedelay
        self.__dirpin__.off()
        self.__steppin__.on()

        self.__maxstep__ = 90
        self.__minstep__ = -90
        self.__curstep__ = 0

        self.__pulseorder__ = 1

    #private: give a pulse into step pin
    def __pulse__(self):
        if self.__pulseorder__:
            self.__steppin__.off()
            time.sleep_us(self.__pulsedelay__)
            self.__steppin__.on()
        else:
            self.__steppin__.on()
            time.sleep_us(self.__pulsedelay__)
            self.__steppin__.off()

        if self.dir():
            self.__curstep__ = self.__curstep__ + 1
        else:
            self.__curstep__ = self.__curstep__ - 1

    #pulse procedence
    def pulseorder(self,neworder = None):
        if neworder != None:
            self.__pulseorder__ = (neworder and 1)
        return self.__pulseorder__

    def pulsedelay(self,newdelay = None):
        if newdelay != None:
            self.__pulsedelay__ = newdelay
        return self.__pulsedelay__


    #set stepper direction
    def dir(self,newdir = None):
        if newdir != None:
            self.__dirpin__.value(newdir and 1)
        return self.__dirpin__.value()

    #step nsteps times
    def step(self,nsteps = 1):
        if nsteps >= 50:
            raise OverStep()

        for i in range(0,nsteps):
            self.__pulse__()

    def step2(self,nsteps = 1):
        if nsteps > 0 and not self.dir():
            self.dir(1)
        if nsteps < 0 and self.dir():
            self.dir(0)
        for i in range(0,abs(nsteps)):
            self.__pulse__()

    #invert direction
    def shiftdir(self):
        self.dir(1 ^ self.__dirpin__.value())
