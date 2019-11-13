#!/usr/bin/python

'''
in order to execute the code you must install the termcolor packet
with the command pip install termcolor
'''



import os
import sys
import time
import multiprocessing
import argparse
import termcolor 



def lecture2():
	text = mq.get()
	if text == "EOF_fin_de_text" :
		mess_count = "There's " + str(mc.get()) + " words in total" 
		print mess_count
	else :
		print text
		array_word = text.split()
		count_word = len(array_word)
		print 
		total_count = mc.get() + count_word 
		mc.put(total_count)



def search(path,pattern):
	fichier = open("texte.txt","r")
	lines = fichier.readlines()
	motif = termcolor.colored(pattern,"red")
	nb_occ = 0
	num_line = 0
	new = ""
	count = 0
	for line in lines :
		num_line += 1
		if pattern in line :
			tab = line.split(pattern)
			count += len(tab) - 1
			for i in tab :
				if i != tab[len(tab)-1] :
					new = new + i + motif
				else :
					new = new + i
			print "line ",num_line," : ",new
			new = ""
	mess_count = "There's " + str(count) + " occurences of : " + pattern
	print mess_count
	file.close






parser = argparse.ArgumentParser()


parser.add_argument("-f", "--file", dest = "filePath", nargs = 1, required = True, help = "Input file path")
parser.add_argument("-s", "--size", dest = "readSize", nargs = "?", default = 2048, const = 1024, type = int, help = "Reading chunks size")
parser.add_argument("-g", "--grep", dest = "pattern_search", help = "Search a pattern in the file and display the lines where it appear, the size option can't be use while using this option")

args = parser.parse_args()




fil = open("texte.txt","r")

mq = multiprocessing.Queue()
mc = multiprocessing.Queue()

mc.put(0)



count = 0

p =[]

while fil:
	extract = fil.read(args.readSize)
	if extract == "" :
		mq.put("EOF_fin_de_text")
		time.sleep(1)
		break	
	else :
		mq.put(extract)
		count = count + 1


for index in range(count):
	if args.pattern_search != None :
		p.append(1)
		p[index] = multiprocessing.Process(target = search, args = (args.filePath[0],args.pattern_search))
		p[index].start()
		break
	p.append(1)
	p[index] = multiprocessing.Process(target = lecture2, args = ())
	p[index].start()
	


for index in range(count):
	p[index].join()

if args.pattern_search == None :
	tmp = mc.get()
	print "There's ", tmp, " words in total"

