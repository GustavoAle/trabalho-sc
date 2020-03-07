from math import *
#import machine
import gc
import time

RAD_TO_DEG = 180 / pi

def map2(x,in_min,in_max,out_min,out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


class MPU():
    #metodo de conversao
    @staticmethod
    def bytes_toint(msb, lsb):
        if not msb & 0x80:
            return msb << 8 | lsb
        return ~(((msb << 8) | lsb) ^ 255)

    def __init__(self, i2c, addr=0x68):
        #i2c
        self.__iic = i2c
        self.__addr = addr

        #variaveis de tempo
        self.__current_time = 0
        self.__previous_time = 0

        #divisores
        self.__accl_div = 16384
        self.__gyro_div = 131

        #erros
        self.__accl_error_x = 0
        self.__accl_error_y = 0
        self.__accl_error_z = 0

        self.__gyro_error_x = 0
        self.__gyro_error_y = 0
        self.__gyro_error_z = 0

        #angulos
        self.__roll = 0
        self.__pitch = 0
        self.__yaw = 0

        self.__accl_x = 0
        self.__accl_y = 0
        self.__accl_z = 0

        self.__gyro_x = 0
        self.__gyro_y = 0
        self.__gyro_z = 0

        #reseta o sensor
        self.write(bytearray([107,0]))

    #escreve no iic
    def write(self,data):
        self.__iic.start()
        self.__iic.writeto(self.__addr, data)
        self.__iic.stop()

    #le do iic
    def read(self,register,bytes):
        self.__iic.start()
        ret = self.__iic.readfrom_mem(self.__addr,register,bytes)
        self.__iic.stop()

        return ret

    def get_raw_values(self):
        return self.read(0x3B,14)

    def get_values2(self):
        raw = self.read(0x3B,6)
        axis_X = raw[0]<<8|raw[1]
        axis_Y = raw[2]<<8|raw[3]
        axis_Z = raw[4]<<8|raw[5]
        xAng = map2(axis_X,265,402,-90,90)
        yAng = map2(axis_Y,265,402,-90,90)
        zAng = map2(axis_Z,265,402,-90,90)
        x = RAD_TO_DEG * (atan2(-yAng, -zAng)+pi)

        return x
