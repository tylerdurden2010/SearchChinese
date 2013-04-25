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


#pchinese=re.compile('([\u4e00-\u9fa5]+)+?')
#f = codecs.open('data1.txt','r','utf-8')
pchinese=re.compile('([^a-zA-Z\\\/`!@#$%^&*()_+-=~\"\;\'?\>\[\]\{\}<>,.]+)+?')
filepath = open("c:\\test.txt")
for path in filepath.readlines():
	path = path.strip('\n')
	#print path
	f = open(path)
	fw = open("c:\data2.txt","ab")
	test = ['\n']
	for line in f.readlines():
		m = pchinese.findall(str(line))
		print m
		if m:
			m = JudgeBlank(m)
			if (test != m):
				str1 = ''.join(m)
				str2=str(str1)
				if ('\n' != str2):
					str2 = str2.rstrip()+('\n')
				fw.write(str2)
f.close()
fw.close()