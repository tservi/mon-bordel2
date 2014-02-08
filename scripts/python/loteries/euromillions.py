# coding=UTF-8
# 
# http://www1.loterie.ch/games/tirage/euro_millions/print.php?dt1=2004-01-01&dt2=2020-01-01
#
# Doc :
#
# socket :
# http://docs.python.org/library/asyncore.html#asyncore.dispatcher.bind 
# http://www.pythonprasanna.com/Papers%20and%20Articles/Sockets/tcpclient_py.txt
#

import socket

class record(object):
	
	def __init__(self,date,c1,c2,c3,c4,c5,s1,s2):
		self.date=date
		self.c=[int(c1),int(c2),int(c3),int(c4),int(c5)]
		self.s=[int(s1),int(s2)]
	
	def somme(self):
		ret=0
		for x in self.c:
			ret+=x
		for x in self.s:
			ret+=x
		return ret

	def moyenne(self):
		return self.somme()/(len(self.c)+len(self.s))
	
	def toString(self):
		return str(self.date)+':'+str(self.c)+'-'+str(self.s)

	def find(self, n1,n2,n3,n4,n5,ns1,ns2):
		return [[n1,n2,n3,n4,n5],[ns1,ns2]] in [[self.c, self.s]]


def searchList():
	host='www1.loterie.ch'
	port=80
	path='/games/tirage/euro_millions/print.php?dt1=2004-01-01&dt2=2020-01-01'
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host,port))
	s.send('GET '+path+' HTTP/1.0\r\nhost: '+host+'\r\n\r\n')
	myF=s.makefile()
	myDatas=myF.read()
	print myDatas
	f=open("euromillion.list.txt",'w+')
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



f=open('euromillion.list.txt.bak','r')
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
newBuffer=buffer[3:-2]
#print newBuffer

allRecords=[]
for x in range(0,len(newBuffer)/8):
	allRecords.append(record( newBuffer[8*x],newBuffer[8*x+1],newBuffer[8*x+2],newBuffer[8*x+3],newBuffer[8*x+4],newBuffer[8*x+5],newBuffer[8*x+6],newBuffer[8*x+7]))	


total=0

allSums={}
n=[2,15,17,26,40]
s=[5,7]
for record in allRecords:
	if record.find(4,13,19,23,38,2,3):
		print record.date
	#somme=record.somme()
	#if allSums.has_key(somme):
	#	allSums[somme]+=1
	#else:
	#	allSums[somme]=1
	#total+=record.somme()



#test='<td ....>bla bla bla</td>'
#extract=''
#if test.find('<td')>=0:
#	index=test.find('>')
#	extract=test[index+1:len(test)]
#	print extract

#print removeTag(test)
