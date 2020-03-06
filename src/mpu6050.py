from math import *
#import machine
import gc
import time

class MPU():
    @staticmethod
    def bytes_toint(firstbyte, secondbyte):
        if not firstbyte & 0x80:
            return firstbyte << 8 | secondbyte
        return - (((firstbyte ^ 255) << 8) | (secondbyte ^ 255) + 1)

    def __init__(self, i2c, addr=0x68):
        self.__iic = i2c
        self.__addr = addr
        self.__accl_error_x = 0
        self.__accl_error_y = 0
        self.__gyro_error_x = 0
        self.__gyro_error_y = 0
        self.__gyro_error_z = 0
        self.__current_time = 0
        self.__previous_time = 0
        
        self.__accl_div = 16384
        self.__gyro_div = 131

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
        
        
        
        self.write(bytearray([107, 0]))

    def write(self,data):
        self.__iic.start()
        self.__iic.writeto(self.__addr, data)
        self.__iic.stop()

    def read(self,register,bytes):
        self.__iic.start()
        ret = self.__iic.readfrom_mem(self.__addr,register,bytes)
        self.__iic.stop()

        return ret 

    def get_raw_values(self):
        return self.read(0x3B,14)

    def get_ints(self):
        b = self.read(0x3B,14)
        c = []
        for i in b:
            c.append(i)
        return c

    def get_values(self):
        raw_ints = self.get_raw_values()
        vals = {}
        vals["AcX"] = self.bytes_toint(raw_ints[0], raw_ints[1])
        vals["AcY"] = self.bytes_toint(raw_ints[2], raw_ints[3])
        vals["AcZ"] = self.bytes_toint(raw_ints[4], raw_ints[5])
        #vals["Tmp"] = self.bytes_toint(raw_ints[6], raw_ints[7]) / 340.00 + 36.53
        vals["GyX"] = self.bytes_toint(raw_ints[8], raw_ints[9])
        vals["GyY"] = self.bytes_toint(raw_ints[10], raw_ints[11])
        vals["GyZ"] = self.bytes_toint(raw_ints[12], raw_ints[13])
        return vals  # returned in range of Int16
        # -32768 to 32767

    def val_test(self,delay):  # ONLY FOR TESTING! Also, fast reading sometimes crashes IIC
        from time import sleep
        while 1:
            print(self.get_values())
            sleep(delay)

    def calculate_imu_error(self):
        c=0
        AccErrorX = 0
        AccErrorY = 0

        while (c < 200):
            raw = self.read(0x3B,6)
            AccX = (raw[0] << 8 | raw[1]) / self.__accl_div
            AccY = (raw[2] << 8 | raw[3]) / self.__accl_div
            AccZ = (raw[4] << 8 | raw[5]) / self.__accl_div

            ## Sum all readings
            AccErrorX = AccErrorX + ((atan((AccY) / sqrt(pow((AccX), 2) + pow((AccZ), 2))) * 180 / pi))
            AccErrorY = AccErrorY + ((atan(-1 * (AccX) / sqrt(pow((AccY), 2) + pow((AccZ), 2))) * 180 / pi))
            c = c + 1

        ##Divide the sum by 200 to get the error value
        self.__accl_error_x = AccErrorX / 200 
        self.__accl_error_y = AccErrorY / 200 
        
        c = 0
        ## Read gyro values 200 times
        GyroErrorX = 0
        GyroErrorY = 0
        GyroErrorZ = 0

        while (c < 200):
            raw = self.read(0x43,6)
            GyroX = raw[0] << 8 | raw[1]
            GyroY = raw[2] << 8 | raw[3]
            GyroZ = raw[4] << 8 | raw[5]
            ## Sum all readings
            GyroErrorX = GyroErrorX + (GyroX / self.__gyro_div)
            GyroErrorY = GyroErrorY + (GyroY / self.__gyro_div)
            GyroErrorZ = GyroErrorZ + (GyroZ / self.__gyro_div)
            c = c + 1

        ##Divide the sum by 200 to get the error value
        self.__gyro_error_x = GyroErrorX / 200
        self.__gyro_error_y = GyroErrorY / 200
        self.__gyro_error_z = GyroErrorZ / 200
        gc.collect()


    def get_filtered_values(self):
        # Start with register 0x3B (ACCEL_XOUT_H)
        raw = self.read(0x3B,6)
        #Read 6 registers total, each axis value is stored in 2 registers
        ##For a range of +-2g, we need to divide the raw values by 16384, according to the datasheet
        AccX = (raw[0] << 8 | raw[1]) / self.__accl_div # X-axis value
        AccY = (raw[2] << 8 | raw[3]) / self.__accl_div # Y-axis value
        AccZ = (raw[4] << 8 | raw[5]) / self.__accl_div # Z-axis value

        # Calculating Roll and Pitch from the accelerometer data
        self.__accl_x = (atan(AccY / sqrt(pow(AccX, 2) + pow(AccZ, 2))) * 180 / pi) - self.__accl_error_x
        self.__accl_y = (atan(-1 * AccX / sqrt(pow(AccY, 2) + pow(AccZ, 2))) * 180 / pi) - self.__accl_error_y
        # === Read gyroscope data === #
        self.__previous_time = self.__current_time        # Previous time is stored before the actual time read
        self.__current_time = time.ticks_us()            # Current time actual time read
        elapsed_time = (self.__current_time - self.__previous_time) / 1000000 # Divide by 1000 to get seconds
        
        raw = self.read(0x43,6)
        
        # For a 250deg/s range we have to divide first the raw value by 131.0, according to the datasheet
        GyroX = (raw[0] << 8 | raw[1]) / self.__gyro_div 
        GyroY = (raw[2] << 8 | raw[3]) / self.__gyro_div
        GyroZ = (raw[4] << 8 | raw[5]) / self.__gyro_div
        # Correct the outputs with the calculated error values
        GyroX = GyroX - self.__gyro_error_x # GyroErrorX ~(-0.56)
        GyroY = GyroY - self.__gyro_error_y # GyroErrorY ~(2)
        GyroZ = GyroZ - self.__gyro_error_z # GyroErrorZ ~ (-0.8)

        # Currently the raw values are in degrees per seconds, deg/s, so we need to multiply by sendonds (s) to get the angle in degrees
        self.__gyro_x = self.__roll + (GyroX * elapsed_time) # deg/s * s = deg
        self.__gyro_y = self.__pitch + (GyroY * elapsed_time)
        #self.__gyro_z = self.__yaw + (GyroZ * elapsed_time)
        
        # Complementary filter - combine acceleromter and gyro angle values
        self.__roll = 0.90 * self.__gyro_x + 0.10 * self.__accl_x
        self.__pitch = 0.90 * self.__gyro_y + 0.10 * self.__accl_y
        #self.__yaw = 0.90 * self.__gyro_z + 0.10 * self.__accl_z 

        

        