#!/usr/bin/python

import os
import sys
import getopt #libreria que me permite ingresar por consola al archivo con el que quiero interactuar

opc, argu = getopt.getopt(sys.argv[1:],'nf:') #sys.argv estoy suprimiendo no me muestra la ruta del archivo codeado.
                                              #preguntar porque se pone getopt.getopt
                                              #preguntar que es bien lo que hace el nf:
print opc

for i in opc:
    if i[0] == "-f": #siempre que en el primer lugar sea -f hacer:
        archivo = i[1] #archivo vendria siendo el que se ingreso

fdo = os.open(archivo, os.O_RDONLY)

EOF = False
arleido = ""
arleido2 = ""

while EOF == False:
    arleido = os.read(fdo, 1024)
    arleido2 = arleido2 + arleido
    if len(arleido)!=1024: #el len cuenta el peso de la variable arleido
        EOF = True

os.close(fdo)

print arleido2
#ejecuto mi codigo, puedo poner el archivo o ruta que quiero abrir, me muestra las opciones y puedo abrirlo para leerlo