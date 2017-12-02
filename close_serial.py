import serial
ser = serial.Serial('COM7', 9600, timeout=1)
ser.close()
