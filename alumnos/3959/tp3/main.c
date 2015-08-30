//@anaquinpm
//El padre lee la entrada STDIN y lo carga en ShMem. Dos Hijos deben procesar la información
//y reemplazar las palabras prohibidas por asteriscos.
//El padre debera mostrar por STDOUT el resultado de lo procesado

#include <sys/types.h>	//shm
#include <sys/mman.h>	//shm
#include <semaphore.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/wait.h>
#include <unistd.h>	//getopt
#include <stdio.h>	
#include <stdlib.h>	//exit
#include <string.h> 	//strcpy
#include "func.h"
#include "hijo.h"

char *words;
char *input;
sem_t * sp;

int main(int argc, char *argv[]){
	int n,fd,c=0;
	int m_sh= sizeof(char) * BUF_SIZE;
	int m_size= m_sh+sizeof(sem_t);
	void * addr;				 //punteros a ShMem para que escriban los hijos
	char buff[BUF_SIZE];

	if((fd=shm_open("/shm",O_CREAT| O_RDWR |O_TRUNC,0666))==-1) exit(EXIT_FAILURE);	//crea/abre un objeto shm
	if((ftruncate(fd,m_size))==-1) exit(EXIT_FAILURE); 		//le doy el tamaño para la shm a crear
	addr = mmap(NULL,m_size,PROT_READ | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS,fd,0);
	if (addr==MAP_FAILED) exit (EXIT_FAILURE);

	sp = (sem_t *) addr;
	addr+=sizeof(sem_t);
	input= (char *)addr;	

	if (((sem_init(sp,1,0))==-1)) exit (EXIT_FAILURE); 

	if((c=getopt(argc,argv,"p:"))!=-1 && argc==3){
		words=argv[2];				//palabras que vamos a buscar
		switch(fork()){
			case -1:
				perror("fork: ");
				exit(EXIT_FAILURE);
			case 0:
				hijo();
				return 0;
			default:	/*--------------------Padre-------------------------*/
				if((n=read(STDIN_FILENO,buff,m_sh))>0){
					strcpy(input,buff);		//agrego el \0 al final de lo leido
					sem_post(sp);
					wait(NULL); 			//espero al hijo
					write(STDOUT_FILENO,input,n);
				}
				sem_destroy(sp);
				shm_unlink("/shm");		//libera la shm
				return 0;
		}		
	}	
	printf("Modo de uso:\t cat mensaje.txt | ./tp3 -p <palabras,a,filtrar>\n");
	exit(EXIT_FAILURE);
}
