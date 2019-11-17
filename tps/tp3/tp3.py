import os,sys,thread,socket
from utils.help import get_options
from multiprocessing import Process, Queue
from datetime import datetime,time
import os

#********* CONSTANT VARIABLES *********
BACKLOG = 50            # how many pending connections queue will hold
MAX_DATA_RECV = 999999  # max number of bytes we receive at once
DEBUG = True            # set to True to see the debug msgs
BLOCKED = []            # just an example. Remove with [""] for no blocking at all.

#**************************************
#********* MAIN PROGRAM ***************
#**************************************
def comparar_tiempo(start,end):
    a=start=datetime.strptime(inicio,'%H:%M:%S').time()
    b=datetime.strptime(fin,'%H:%M:%S').time()
    #datetime.now().time()
    #print actual
    if  a > datetime.now().time() or datetime.now().time() < b:
	print "no internet"
    else:
        print "si internet"


def main(start,end,port):
    comparar_tiempo(inicio,fin)
  

    # host and port info.
    host = ''               # blank for localhost
    
    print "Proxy Server Running on ",host,":",port

    try:
        # create a socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # associate the socket to host and port
        s.bind((host, port))

        # listenning
        s.listen(BACKLOG)
    
    except socket.error, (value, message):
        if s:
            s.close()
        print "Could not open socket:", message
        sys.exit(1)

    # get the connection from client
    while 1:
        conn, client_addr = s.accept()

        # create a thread to handle request
        thread.start_new_thread(proxy_thread, (conn, client_addr))
        
    s.close()
#************** END MAIN PROGRAM ***************

def printout(type,request,address):
    if "Block" in type or "Blacklist" in type:
        colornum = 91
    elif "Request" in type:
        colornum = 92
    elif "Reset" in type:
        colornum = 93

    print "\033[",colornum,"m",address[0],"\t",type,"\t",request,"\033[0m"

#*******************************************
#********* PROXY_THREAD FUNC ***************
# A thread to handle request from browser
#*******************************************
def proxy_thread(conn, client_addr):

    # get the request from browser
    request = conn.recv(MAX_DATA_RECV)

    # parse the first line
    first_line = request.split('\n')[0]

    # get url
    url = first_line.split(' ')[1]

    for i in range(0,len(BLOCKED)):
        if BLOCKED[i] in url:
            printout("Blacklisted",first_line,client_addr)
            conn.close()
            sys.exit(1)


    printout("Request",first_line,client_addr)
    # print "URL:",url
    # print
    
    # find the webserver and port
    http_pos = url.find("://")          # find pos of ://
    if (http_pos==-1):
        temp = url
    else:
        temp = url[(http_pos+3):]       # get the rest of url
    
    port_pos = temp.find(":")           # find the port pos (if any)

    # find end of web server
    webserver_pos = temp.find("/")
    if webserver_pos == -1:
        webserver_pos = len(temp)

    webserver = ""
    port = -1
    if (port_pos==-1 or webserver_pos < port_pos):      # default port
        port = 80
        webserver = temp[:webserver_pos]
    else:       # specific port
        port = int((temp[(port_pos+1):])[:webserver_pos-port_pos-1])
        webserver = temp[:port_pos]

    try:
        # create a socket to connect to the web server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        s.connect((webserver, port))
        s.send(request)         # send request to webserver
        
        while 1:
            # receive data from web server
            data = s.recv(MAX_DATA_RECV)
            
            if (len(data) > 0):
                # send to browser
                conn.send(data)
            else:
                break
        s.close()
        conn.close()
    except socket.error, (value, message):
        if s:
            s.close()
        if conn:
            conn.close()
        printout("Peer Reset",first_line,client_addr)
        sys.exit(1)
#********** END PROXY_THREAD ***********
    
if __name__ == '__main__':
#parte nueva
    options = get_options()    
    in_queue = Queue()
    out_queue = Queue()
    fd = open(options['file'])
    puerto = options['port']
    print puerto
    inicio = fd.readline()
    inicio[1:7] 
    inicio=inicio.replace("\n",'')
    fin = fd.readline()
    fin[1:7]
    fin=fin.replace("\n",'')
    print inicio
    main(inicio,fin,puerto)
    

    




