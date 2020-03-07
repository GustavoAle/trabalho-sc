# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos
import gc
import machine
from machine import Pin, I2C
from mpu6050 import MPU
from machine import Timer
import stepper, basics

machine.freq(160000000)

iic = I2C(scl=Pin(14),sda=Pin(12))
m = MPU(iic,iic.scan()[0])
s = stepper.Stepper()

gc.collect()
