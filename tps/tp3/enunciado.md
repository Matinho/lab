# TP3


# Enunciado

Fecha de entrega: 24/09/2019


### Problema

Se quiere que los alumnos de Computación2 presten mas atención en clases, para lo cual, NO podrán acceder a 
Internet en el horario de cursado  :-).

Se decide usar un proxy multiprocesos o multihilos para conrolar el tráfico a Internet. 


### Requerimientos

* La aplicación debe contener como mínimo 3 funciones u objetos.
* Debe procesar los métodos GET y POST.
* Debe tener un archivo de configuración, donde indica el horario en que deniega o permite el acceso a internet.
* Debe justificar porque usa el modulo multiprosessing o threading.
* Debe manejar los errores.


#### Ejemplo modo de uso

~~~~~~~~~~~~~~~~~~~
./tp3.py -f <archivo> -p <puerto_de_escucha>

./tp3.py (en caso de no especificar, deberá usar parámetros por defecto

~~~~~~~~~~~~~~~~~~~


### Objetivos

* Manejo de archivos (apertura, escritura y cierre).
* Creación de procesos/hilos.
* Manejo de socket servidor y socket cliente.
* Uso de mecanismos de IPC.

### Bonus Track1

Se deberá registrar la ip del usuario que quiera navegar y sea bloqueado por el proxy

### Bonus Track2

Se deberá validar el nombre de usuario para acceder a internet

