##bibliotecas
from msilib.schema import Class
import serial
import sys
from digi.xbee.devices import XBeeDevice

MAX_PORTAS = 32
PORT = 'COM5'
BIT_RATE = 9600

arduino = serial.Serial(PORT,BIT_RATE)

while True:
    linha = str(arduino.readline())
    print(linha)
