
#!/usr/bin/python
from utils.help import get_options
from multiprocessing import Process, Queue
from PIL import Image
from urllib import urlopen
from StringIO import StringIO
from random import randint,uniform, random

contador=0
def crear_hijos(x):
    
    hijos = []

    for i in range(int(len(x))):
        
        hijo = Process(target=get_Imagen(x[i]))
        hijos.append(hijo)
        hijo.start()
    return hijos

def get_Imagen(URL):
  print URL
  data=urlopen(URL).read()
  file= StringIO(data)
  img = Image.open(file)
  nombre= img.filename
  random= str(randint(0,1000))
  img.save(random+".png",format="PNG")

  convertir_Imagen(img,random)


def convertir_Imagen(img,random):
  data = img.getdata()
  print "nombre del archivo dentro de convertir"+img.filename
  r = [(d[0],0,0) for d in data ]
  g = [(0,d[0],0) for d in data ]
  b = [(0,0,d[0]) for d in data ]
  img.putdata(r)
  img.save(random+'_r'+'.png',format="PNG")
  img.putdata(g)
  img.save(random+'_g'+'.png',format="PNG")
  img.putdata(b)
  img.save(random+'_b'+'.png',format="PNG")

if __name__ == "__main__":
    
    options = get_options()    
    in_queue = Queue()
    out_queue = Queue()
    URL=str(options['url'])
    print URL
    URL=URL.replace('[','')
    URL=URL.replace(']','')
    URL=URL.replace("'",'')
    
    x=URL.split(',')

    print len(x)
    hijos = crear_hijos(x)
       

    for hijo in hijos:
        hijo.join()
