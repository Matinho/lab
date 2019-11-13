#!/usr/bin/python3
""" TP2 para ejercitar sincronizacion y sus problemas"""
import threading
import time
import random

lugares_bote = []
viajes = 0

def hincha_river():
    """ Implementar funcion para subir al bote ....si es que se puede ..."""
    print("vamos river")

def hincha_boca():
    """ Implementar funcion para subir al bote ....si es que se puede ..."""
    print("vamos boca")

def barra_brava_river():
    """ Generacion de hinchas de River"""
    while viajes < 20:
        time.sleep(random.randrange(0, 5))
        r = threading.Thread()
        r.start()

def barra_brava_boca():
    """ Generacion de hinchas de Boca"""
    while viajes < 20:
        time.sleep(random.randrange(0, 5))
        b = threading.Thread()
        b.start()

t1 = threading.Thread()
t2 = threading.Thread()

print("terminaron los viajes ")

