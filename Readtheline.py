#using for reading the specia lines and write into a files
import linecache,os,sys
reload(sys)
sys.setdefaultencoding('utf8')
def Convert(strings):
	return strings.encode('gb18030')

#kernel function.read the special lines	
def getline(thefilepath, desired_line_number):
	if desired_line_number < 1: return ''
	for current_line_number, line in enumerate(open(thefilepath)):
		if current_line_number == desired_line_number - 1 : return line
	return ''

for filepoint in range(1,1074):
	allineed = open("C:\\Users\\username\\Desktop\\1068\\"+str(filepoint)+".txt",'w')	
	for i in range (308,334):
		filepath = "C:\\Users\\username\\Desktop\\1068\\" + str(filepoint)
		allineed.write(Convert(getline(filepath,i)))