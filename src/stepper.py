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

    #invert direction 
    def shiftdir(self):
        self.dir(1 ^ self.__dirpin__.value())
