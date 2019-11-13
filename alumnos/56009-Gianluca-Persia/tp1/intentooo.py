#!/usr/bin/python

import os
import sys
import multiprocessing
import getopt

def open(queue, size, path):
    EOF = False
    
    fd = os.open(path, os.O_RDONLY) #lectura

    while not EOF: #bucle leer bloques y particiones
        read = os.read(fd, size) #lectura de bytes
        queue.put(read) #lo que se lee lo coloco en cola
        '''sale del bucle una vez completada la lectura en su totalidad'''
        if len(read)<size:
            EOF = True
        os.close(fd) #cierro

def count(reading): #contar los elementos
    for caracter in "\n":
        reading = reading.replace(caracter, " ") #recorro y reemplazo
    return len(reading.split()) #devuelvo la cantidad de elementos

def queuewords(queue, finalqueue):
    while queue.qsize() != 0: #si la cola tiene algun contenido
        read = queue.get() #guardo los elementos de la cola
        words = count(reading) #llamo a count
        finalqueue.put(words) #coloco en una nueva cola la cantidad de elementos
    return #devuelvo

def childprocess(): #procesos hijos
    process = [] #declaro
    for counter in range(processnumber): #coloco la cantidad de procesos en lista
        sonsprocess = multiprocessing.Process(target = queuewords, args = (entry, exitt)) #llamo a procesos hijos
        process.append(sonsprocess) #agrego a lista
        sonsprocess.start() #ejecuto
    return process #lista

def united(processlist):
    for p in processlist: #recorro la lista
        p.join() #bloqueo

def help(): #ayuda
    print "Instrucciones:"
    mesagge = "Para ejecutar usar la siguiente linea de codigo: ./nombrearchivo.py -f [ruta o nombre del archivo(en caso de estar posicionado en ruta)]"
    mesagge = "-p [cantidad de procesos durante la ejecucion]"
    mesagge = "-n [bytes de tamaño]"
    print mesagge
    print "Puede usar lo siguiente ./intento.py -f prueba.txt -p 2 -n 2048"
    exit(0) #salir

entry = multiprocessing.Queue() #creacion multiprocesamiento
exitt = multiprocessing.Queue()
'''getopot para ingresar datos por consola'''
opc, arg = getopt.getopt(sys.argv[1:], "f:n:p:h")
'''con este bucle se localiza el panorama :)'''
value = 0
processnumber = 2
filepath = ""

for i in opc:
    if i[0] == "-f": #localizacion del archivo
        filepath = i[1]
    if i[0] == "-p": #cantidad de procesos
        processnumber = int(i[1])
    if i[0] == "-n": #cantidad de bytes para la lectura por bloques
        value = int(i[1])
    if i[0] == "-h": #ayuda del usuario
        help()

processlist = sonsprocess() #invoco funcion

read(int (value), entry, filepath) #invoco funcion

united(processlist) #invoco funcion

nwords = 0 #inicio contador en 0

while exitt.qsize() != 0: #si la cola de salida contenga algo
    nwords = nwords + int(exitt.get()) #con esto voy sumando la cantidad de palabras de la cola
    print "Cantidad de palabras encontradas: ", nwords