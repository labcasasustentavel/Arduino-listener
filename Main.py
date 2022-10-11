##bibliotecas
from msilib.schema import Class
import string
import serial
import sys
from digi.xbee.devices import XBeeDevice
import mysql.connector


MAX_PORTAS = 32
PORT = 'COM4'
BIT_RATE = 9600

config = {
  'user': 'root',
  'password': '251911',
  'host': '127.0.0.1',
  'database': 'lcs_dev',
  'raise_on_warnings': True
}


def db(amb : string,umidade : float,temperatura : float,luminosidade float):
    try:
        cnx = mysql.connector.connect(**config)
    finally:
        cnx.close()


def str_translate(data_str):
    chars = ';:'
    return data_str.translate(str.maketrans('', '', chars))

def amb(serial_str : string):
    serial_str = serial_str.split()
    ambiente = serial_str[1]
    umidade = serial_str[2]
    temperatura = serial_str[3]
    luminosidade = serial_str[4]

    ambiente = str_translate(ambiente)
    umidade = (str_translate(umidade))
    temperatura = (str_translate(temperatura))
    luminosidade = (str_translate(luminosidade))

    umidade = float(umidade)
    print(type(umidade))


arduino = serial.Serial(PORT,BIT_RATE)
while True:
    linha = amb(str(arduino.readline()))