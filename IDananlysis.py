#coding=utf-8 
import os 
import sys 
import re
def JudgeBlank(test):
	i = 0
	for index in range(len(test)):
		if( ' ' in test[index] or '\t' in test[index] ):
			i = i +1
	if (i == len(test) - 1):
		test = ['\n']
		return test
	else:
		return test


fw = open("c:\data2.txt","ab")
pchinese=re.compile('([^a-zA-Z\\\/`!@#$%^&*()_+-=~\"\;\'?\>\[\]\{\}<>,. ]|\d+)+?')
for index in range(1,1074):
    f = open("C:\\Users\\Linquid\\Desktop\\1068\\" +str(index)+".txt")
    test = ['\n']
    for line in f.readlines():
        m = pchinese.findall(str(line))
        #print m
        if m:
            m = JudgeBlank(m)
            if (test != m):
                str1 = ''.join(m)
                str2=str(str1)
                if ('\n' != str2):
                    str2 = str2.rstrip()+('\n')
                
                fw.write(str2)
    fenge = "=====================\n"
    fw.write(fenge)
f.close()
fw.close()