# COMPUTACION II


## TP4

Fecha de entrega: 12/11/2019


### Problema

Realizar una aplicación que a partir de una lista de URLs, parsee los HTMLs de las 
páginas y descargue las imágenes. Si las imágenes son jpg, debe convertirlas a ppm
para procesarlas. Una vez convertidas, la aplicación deberá generar una imagen por
cada componente RGB.


### Requerimientos

* La aplicación debe contener como mínimo 3 módulos.
* Debe procesar las opciones con getopt (agregar una opcion de ayuda) o con argparse.
* Debe usar los módulos Multiprocessing.Pool, ThreadPoolExecutor o ProcessPoolExecutor
para descargar las páginas y descomponga en componentes RGB.
* Debe manejar los errores.


#### Ejemplo modo de uso

~~~~~~~~~~~~~~~~~~~
./tp4.py -u http://www.example.com,http://www.example1.com,http://www.example2.com
~~~~~~~~~~~~~~~~~~~


### Objetivos

* Manejo de archivos (apertura, escritura y cierre).
* Manejo de procesos o hilos.
* Manejo de programación paralela y/o asíncrona.

TIP: para conversión de tipo de imágenes puede usar la Python Imaging Library (pillow)

