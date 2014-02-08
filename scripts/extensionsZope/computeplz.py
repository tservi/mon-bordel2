# script utilise pour parcourir un fichier

import os

print os.getcwd()

ff=open('plz.csv','r+')
lplz0=[]
lplz0=ff.readlines()
ff.close()

lplz1=[]
for x in lplz0:
   lplz1.append(x.split('\r\n')[0])
   
#print l1
lplz2=[]
for x in lplz1[1:len(lplz1)]:
   z=x.split(';')
   lplz2.append([z[0],z[1],z[2],z[3],int(z[4])])
   
print lplz2
#lplz3=[]
#for x in lplz2[1:len(lplz2)]:
#    print int(x[4])