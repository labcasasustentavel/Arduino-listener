##bibliotecas
from msilib.schema import Class
import serial
import sys
from digi.xbee.devices import XBeeDevice

MAX_PORTAS = 32 # Número máximo de portas para verificação

class Portas :
    def getPortsInUse():
        for p in ['COM%s' % (i + 1) for i in range(Portas.MAX_PORTAS)]:
            try: 
                s =  serial.Serial(p)
                s.close()
                yield s.name
            except (OSError, serial.SerialException) :
                pass
