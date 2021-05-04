from ColaFIFO import *
from ColaFIFOConTamanio import *
import threading
import random
import logging
import time

cola= ColaFIFO()

colaConTamanio = ColaFIFOConTamanio(10)

logging.basicConfig(format="%(asctime)s.%(msecs)02d [%(threadName)s] - %(message)s", datefmt= "%H:%M:%S", level= logging.INFO)


class Hilo (threading.Thread):

    def __init__(self, name, cola, retardo ):
        threading.Thread.__init__(self, name=name,args=(cola,retardo))
        self.name=name
        self.miCola= cola
        self.retardo = retardo

    def run(self):
        if self.name == "Productor":
            self.loopInfinitoInserta()
        else:
            self.loopInfinitoExtrae()

    def loopInfinitoInserta(self):

        while True:
            numero = random.randint(0,100)
            self.miCola.insertar(numero)
            logging.info("Se ingreso el numero: {:.0f}".format(numero))
            time.sleep(self.retardo)
            #print(self.miCola.cantidad_elementos())

    def loopInfinitoExtrae(self):

        while True:
            numero = self.miCola.extraer()
            logging.info("Se extrajo el numero: {:.0f}".format(numero))
            time.sleep(self.retardo)


productor = Hilo('Productor', colaConTamanio, 1)

consumidor = Hilo('Consumidor', colaConTamanio, 1)

productor.start()
consumidor.start()