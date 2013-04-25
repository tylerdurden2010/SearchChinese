import os
import sys
filea = open("../a.txt")
fileb = open("../b.txt")
linea = filea.readlines()
lineb = fileb.readlines()
for index in range(len(linea)):
	linea[index] = linea[index].rstrip()
	lineb[index] = lineb[index].rstrip()
	command = "sed -i \"s/"+linea[index]+"/"+lineb[index] + "/g\" `grep -rl xlog ./*`"
	#os.system('ls')c
	os.system(command)
	#print command
	#raw_input("break")