# COMPUTACION II


## TP1

Fecha de entrega: 7/05/2019


### Problema

Realizar una aplicación que abra y lea un archivo indicado por la opcion "-f archivo".

El proceso padre debe lanzar dos procesos hijos para procesar el archivo. Debe ir leyendo el archivo por bloques de n bytes indicadas por la opcion "-n valor", y alimentar una cola de mensaje con ellos.

Cada proceso hijo debe contar la cantidad de palabras que recibe por la cola de mensajes.

Cuando el proceso padre termina de leer el archivo, debe cerrar y esperar que los hijos terminen de trabajar.

El proceso padre debe mostrar al terminar, la cantidad total de palabras por la salida estándar (STDOUT).


### Requerimientos

* La aplicación debe contener como mínimo 3 funciones.
* Debe procesar las opciones con getopt (agregar una opcion de ayuda) o con argparse.
* Debe usar el modulo multiprosessing.
* Debe manejar los errores.


#### Ejemplo modo de uso

~~~~~~~~~~~~~~~~~~~
./tp1.py -f <archivo> -n <tamaño_bloque>

./tp1.py -f /etc/services -n 1024

palabras totales: 2615
~~~~~~~~~~~~~~~~~~~


### Objetivos

* Manejo de archivos (apertura, escritura y cierre).
* Creación de procesos.
* Uso de mecanismos de IPC.

### Bonus Track

Se adicionará la opcion -p nro , para indicar cuantos hijos se crearán para procesar el archivo 
