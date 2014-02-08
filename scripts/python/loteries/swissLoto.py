# coding=UTF-8
# 
# http://www1.loterie.ch/games/tirage/swiss_lotto/print.php?dt1=1910-01-01&dt2=2020-01-01
#
# Doc :
#
# socket :
# http://docs.python.org/library/asyncore.html#asyncore.dispatcher.bind 
# http://www.pythonprasanna.com/Papers%20and%20Articles/Sockets/tcpclient_py.txt
#

import socket

def findMin(tab):
	if len(tab)>0:
		min=tab[0]
		for x in tab:
			if x<min:
				min=x
		return min
	else:
		return False

class record(object):
	
	def __init__(self,date,c1,c2,c3,c4,c5,c6,c7):
		self.date=date
		originalRecord=[int(c1),int(c2),int(c3),int(c4),int(c5),int(c6),int(c7)]
		record=[]
		for index in range(0, len(originalRecord)):
			min=findMin(originalRecord)
			originalRecord.remove(min)
			record.append(min)
		self.c=record
	
	def somme(self):
		ret=0
		for x in self.c:
			ret+=x
		return ret

	def moyenne(self):
		return self.somme()/(len(self.c))
	
	def toString(self):
		ret=''
		ret+=str(self.date)
		ret+=' : '
		for x in self.c:
			ret+='%2d '%(x)
		return ret


def searchList():
	host='www1.loterie.ch'
	port=80
	path='/games/tirage/swiss_lotto/print.php?dt1=1910-01-01&dt2=2020-01-01'
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host,port))
	s.send('GET '+path+' HTTP/1.0\r\nhost: '+host+'\r\n\r\n')
	myF=s.makefile()
	myDatas=myF.read()
	print myDatas
	f=open("swissLoto.list.txt",'w+')
	f.write(myDatas)
	f.close()


def removeTag(s):
	begin=s.find('<')
	if begin>=0:
		ret=''
		if begin>0:
			ret+=s[0:begin]
		sub=s[begin+1:len(s)]
		end=sub.find('>')
		if end>=0:
			ret+=sub[end+1:len(sub)]
			return removeTag(ret)
		else:
			return s
	else:
		return s


#searchList()


f=open('swissLoto.list.txt.bak','r')
myDatas=f.read()
buffer=[]
addInBuffer=False
for line in myDatas.split('\n'):
	if line.find('<table')>=0:
		#print "begin"
		addInBuffer=True
		buffer=[]
	if line.find('</table')>=0:
		#print "end"
		addInBuffer=False
	if addInBuffer:
		newLine=line.replace('\t','')
		if newLine.find('<td width="50" align=right></td>')>=0:
			newLine='-'
		newLine=removeTag(newLine)
		#newLine=newLine.replace('</td>','')
		#newLine=newLine.replace('</tr>','')
                #newLine=newLine.replace('<td width="50" align=right>','')
		#newLine=newLine.replace('<td width="100" align=right>','')
		#newLine=newLine.replace('<td width="100">','')
		#newLine=newLine.replace('<tr bgcolor="#EEEEEE">','')
		#newLine=newLine.replace('<tr>','')
		#if newLine.find('<td')>=0:
		#	newLine=''
		#if newLine.find('<table')>=0:
		#	newLine=''
		if len(newLine)>0:
			buffer.append(newLine)
f.close()

newBuffer=buffer[4:-2]
#print newBuffer[-40:len(newBuffer)]

allRecords=[]
lineLen=11
for x in range(0,len(newBuffer)/lineLen):
	#if newBuffer[lineLen*x].find('07.03.2007')>=0:	
	#	lineLen=10
	if len(newBuffer)>lineLen*x+7:
		allRecords.append(record( newBuffer[lineLen*x],newBuffer[lineLen*x+1],newBuffer[lineLen*x+2],newBuffer[lineLen*x+3],newBuffer[lineLen*x+4],newBuffer[lineLen*x+5],newBuffer[lineLen*x+6],newBuffer[lineLen*x+7]))	
	#print x, lineLen

total=0

allSums={}
for record in allRecords:
	print record.toString()
	somme=record.somme()
	if allSums.has_key(somme):
		allSums[somme]+=1
	else:
		allSums[somme]=1
	total+=record.somme()

print allSums
print total/len(allRecords)

#test='<td ....>bla bla bla</td>'
#extract=''
#if test.find('<td')>=0:
#	index=test.find('>')
#	extract=test[index+1:len(test)]
#	print extract

#print removeTag(test)

