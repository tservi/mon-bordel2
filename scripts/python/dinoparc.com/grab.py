import socket
myUser='myUserForDinoparc.com'
myPass='myPassForDinoparc.com'
host='www.dinoparc.com'
port=80
path='/'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
s.send('GET '+path+' HTTP/1.0\r\nhost: '+host+'\r\n\r\n')
myF=s.makefile()
myDatas=myF.read()
s.close()
line=''
for x in myDatas.split('\n'):
	if x.find('<form action="')>=0:
		line+=x.replace('\t','')
		

#print line
newPath=line.split('action="')[-1].split('"')[0]
print newPath
newPath+='&login='+myUser+'&pass='+myPass
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
s.send('GET '+newPath+' HTTP/1.0\r\nhost: '+host+'\r\n\r\n')
myF=s.makefile()
myDatas=myF.read()
s.close()
print myDatas
