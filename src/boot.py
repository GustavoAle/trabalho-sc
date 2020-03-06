# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos
import gc
from machine import Pin, I2C
from mpu6050 import MPU
from machine import Timer


iic = I2C(scl=Pin(14),sda=Pin(12),freq=500000)
m = MPU(iic)
m.calculate_imu_error()
m.calculate_imu_error()
tim = Timer(-1)



def get_angles():
    m.get_filtered_values()
    print("Roll: \t{} \tPitch: \t{}".format(m.__roll, m.__pitch))

tim.init(period=100, mode=Timer.PERIODIC, callback=lambda t:get_angles())

gc.collect()
