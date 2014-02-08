#####################################################################
#   python code for the integration of external content in zope     #
#  this file must be named getweb.py and then comes in Extensions   #
#    after you must define  external methods for the  functions     #
#       report your questions to jeantinguelyawais @ gmail.com      #
#                      year created : 2006                          #
#####################################################################


import os
import socket
import sys

path_to_index="/*******/index.txt"

def getwebpage(hostname='', page=''):
  #get the page source code
  val=0
  try:
      my_index=file(path_to_index,'r+') 
  except:
      my_index=file(path_to_index, 'w+')
  try:
      val=int(my_index.read())
  except:
     val=0
  my_index.close()
  PORT=80
  if hostname=='':
     hostname='www.t-servi.com'
  if page=='':
     page='content/index_ger.html'
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((hostname,PORT))
  s.send('GET /'+page+' HTTP/1.1 \r\nhost: '+hostname+'  \r\nUser-Agent: Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; fr; rv:1.8.0.6) Gecko/20060728 Firefox/1.5.0.6 \r\n\r\n')
  my_file=s.makefile()
  s.close()
  val=val+1
  my_index=file(path_to_index,'w+')
  my_index.write(str(val))
  my_index.close()
  my_data=my_file.readlines()
  my_bk=[]
  for x in my_data:
   my_bk.append(str(x).decode('iso-8859-1').encode('utf-8'))
  ret=[hostname,page,my_bk]
  return ret


