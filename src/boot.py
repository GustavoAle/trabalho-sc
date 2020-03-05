# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos
import gc
from machine import Pin, I2C
from mpu6050 import MPU

iic = I2C(scl=Pin(14),sda=Pin(12))
m = MPU(iic)
m.calculate_imu_error()


def get_angles():
    m.get_filtered_values()
    print("Roll: \t{} \tPitch: \t{}".format(m.__roll, m.__pitch))

gc.collect()
