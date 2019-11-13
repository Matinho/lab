#!/usr/bin/python
# -*- coding: utf-8 -*-

from multiprocessing import Process, Queue
import os
import sys
import getopt



def ayuda():
    print("./tp1.py -f <archivo> -n <tamaño_bloque> -p <hijos>")
      
    print('./tp1.py -f /etc/services -n 1024 -p 2\n')
 
def func1():
	a = 0
	while True:
                        leido = mq.get()	
			if leido == "listo":
                            break
			a = a + len(leido.split(" "))

        mqr.put(a)                        

try:
	(opts, args) = getopt.getopt(sys.argv[1:],'hf:n:p:')
except getopt.GetoptError as err:
	print(err)
	sys.exit(2)


if len(opts) != 0:
	for (o,a) in opts:
		if o in ('-h'):
			ayuda()
			sys.exit()
		elif o in ('-f'):
			archivo_origen= sys.argv[2]
		elif o in ('-n'):
			bloque= sys.argv[4]
		elif o in ('-p'):
			hijos= sys.argv[6]
		else:
			ayuda()
			sys.exit(2)
else:
	ayuda()
	sys.exit(2)
print "soy el padre"
print  "el nombre del archivo de origen es: ",archivo_origen
print "el bloque determinado es: ",bloque
print "la cantidad de hijos a crear es: ",hijos

processes = []

fdo = os.open( archivo_origen, os.O_RDONLY )
total = os.stat(archivo_origen).st_size

EOF = False
mq = Queue()
mqr = Queue()


for i in range(int(hijos)):
	p = Process(target=func1, args=())
	processes.append(p)
	p.start()


while EOF == False:
	leido = os.read(fdo, int(bloque))
	print "total leido del archivo: ",len(leido)
	mq.put(leido)
	if len(leido) != int(bloque):
		EOF = True

for process in processes:
    mq.put("listo")
for process in processes:
	process.join()

print "terminaron los hijos"

palabras_totales = 0
while mqr.empty() is False:
	palabras_totales = palabras_totales + mqr.get()

print palabras_totales
