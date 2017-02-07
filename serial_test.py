import serial
import time

ser = serial.Serial(‘/dev/ttyUSB0’,9600,timeout=1) # 9600 is the default Baudrate for SIM900A modem
ser.flush()
ser.write(‘AT+CMGS=6478012349; hello \0XOD\0X0A’) # AT command to call a number using GSM Modem — Edit here
#ser.read(2) # read 2 bytes of data from the serial port
time.sleep(10) # wait for 10 secondsser.write(‘ATH\r’) # Hold the call
ser.close() # close the serial port
