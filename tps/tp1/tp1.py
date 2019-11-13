#!/usr/bin/python

import os
import argparse
from multiprocessing import Process
from multiprocessing import Queue

def ArgsParse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", dest = "archivo", required = True, help = "Nombre del archivo") # it seems like nargs is not required...
    parser.add_argument("-s", "--size", dest = "tamanio", nargs = "?", default = 2048, const = 1024, type = int, help = "Tamanio lectura")
    parser.add_argument("-p", "--process", dest = "procesos", nargs = "?", default = 2, type = int, help = "Cantidad procesos") # it seems like nargs is not required...
    return parser.parse_args()

def CrearProcesos():
    listaProcesos = []
    for numero in range(cantidadProcesos):
        p = Process(target=ContarPalabras, args=(colaResultadoSuma,))
        listaProcesos.append(p)
        p.start()
    return listaProcesos

def LeerArchivo(nombreArchivo,cantidadbytes,colaTextoSplit,cantidadProcesos):
    fd = os.open(nombreArchivo,os.O_RDONLY)
    EOF = True
    indice = 0
    c=0
    while EOF :
        bloque = os.read(fd,cantidadbytes)
        for letra in bloque[::-1]:
            indice = indice +1
            if (letra == " ") or letra == "\n":
                #le agrego el salto de linea porque se me cortaba de nuevo
                i = indice
                indice = 0
                break
        espacio = cantidadbytes - i
        if c==0:
            texto = bloque[0:espacio]
            siguiente = bloque[espacio+1:cantidadbytes]
        if c!=0:
            texto = siguiente+bloque[0:espacio]
            siguiente = bloque[espacio+1:cantidadbytes]
        colaTextoSplit.put(texto.split())
        texto = ""
        c = c + 1
        if len(bloque)<cantidadbytes:
            EOF = False
    os.close(fd)
    for rango in range(cantidadProcesos):
        colaTextoSplit.put("TERMINO")


def ContarPalabras(colaResultadoSuma):
    textoSplit = ""
    suma = 0
    while True:
        textoSplit = colaTextoSplit.get()
        if(textoSplit=="TERMINO"):
            break
        print (textoSplit)
        cantidad = len(textoSplit)
        suma = suma + cantidad
    colaResultadoSuma.put(suma)


def UnirProcesos(lista):
    for pro in lista:
        pro.join()


def MostrarCantidadPalabras():
    suma = 0
    while colaResultadoSuma.empty() is False:
        cantidad_palabras = colaResultadoSuma.get()
        if(cantidad_palabras!=0):
            suma = suma + cantidad_palabras
            #print 'cantidad de palabras del archivo: ', cantidad_palabras
    print ('cantidad de palabras del archivo: ',suma)



if __name__ == "__main__":

    argumento = ArgsParse()
    nombreArchivo = argumento.archivo
    cantidadbytes = argumento.tamanio
    cantidadProcesos = argumento.procesos

    colaTextoSplit = Queue()
    colaResultadoSuma = Queue()

    lista = CrearProcesos()

    LeerArchivo(nombreArchivo,cantidadbytes,colaTextoSplit,cantidadProcesos)

    UnirProcesos(lista)

    MostrarCantidadPalabras() 