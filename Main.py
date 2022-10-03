##bibliotecas
from msilib.schema import Class
import serial
import sys
from digi.xbee.devices import XBeeDevice

MAX_PORTAS = 32
PORT = "COM1"
BIT_RATE = 9600

##check ports
class Portas :
    def getPortsInUse():
        for p in ['COM%s' % (i + 1) for i in range(Portas.MAX_PORTAS)]:
            try: 
                s =  serial.Serial(p)
                s.close()
                yield s.name
            except (OSError, serial.SerialException) :
                pass

##opening device connection
device = XBeeDevice(PORT, BIT_RATE)
try:
    device.open()

    ##Get the XBee protocol
    protocol = device.get_protocol()

    ##Get the operating mode
    operanting_mode = device._get_operating_mode()
finally:
    if device is not None and device.is_open()
        device.close()


