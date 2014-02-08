# script utilise pour parcourrir un fichier csv


import os

print os.getcwd()
print '--------------------------------------------------------------------'

ff=open('nr.txt','r+')
l0=[]
l0=ff.readlines()
ff.close()

l1=[]
for x in l0:
   l1.append(x.split('\r\n')[0])
   
#print l1

l2=[]
for x in l1:
   z=x.split(';')
   l2.append([z[0],z[1][3:len(z[1])],z[2],z[3]])

  
#print l2
 
l3=[]
for x in l2:
   z=x[3].split(',')
   l3.append([x[0],x[1],x[2],z])

      
#print l3

l4=[]
for x in l3:
   z=x[3]
   t=[]
   for y in z:
       u=y.split('-')
       if len(u)==1: 
          m=[int(str(u[0]).replace(' ',''))]
          #t.append(int((str(u).replace(' ','').replace('[','').replace(']','').replace('\'',''))))
       else:
          m=range(int(str(u[0]).replace(' ','')), int(str(u[1]).replace(' ',''))+1)
       for m2 in m:
          t.append(m2)
   l4.append([x[0],x[1],x[2],t])
   
#print l4
l5=[]
for x in l4:
   l5.append(str(x))
   
ff=open('gemeinde.csv','w+')
ff.writelines(l5)
ff.close()


print '--------------------------------------------------------------------'
print '------------------------   controle       --------------------------'
print '--------------------------------------------------------------------'
i=0
for x in l4:
   if int(x[2])!=len(x[3]):
       i=i+1
       print str(i)+' '+x[1]+' ('+x[0]+') not OK ! '+x[2]+' != '+str(len(x[3]))+' ==> '+str(len(x[3])-int(x[2]))+' de trop'
       print x[3]
       print '--------------------------------------------------------------------'
       
 
ff=open('g_nummer.csv','w+')
gn1=[]
for x in l4:
    z=x[3]
    for v in z:
       gn1.append([v,x[1],x[0]]) 

       
       
gn2=[]
for x in gn1:
   gn2.append(str(x[0])+';'+str(x[1]).rstrip().lstrip()+';'+str(x[2])+';\r\n')
   
print gn2          
ff.writelines(gn2)
ff.close() 

#ff=open('plz.txt','r+')
#lplz0=[]
#lplz0=ff.readlines()
#ff.close()

#lplz1=[]
#for x in lplz0:
#   lplz1.append(x.split('\r\n')[0])
   
#print l1
#lplz2=[]
#for x in lplz1[1:len(lplz1)]:
#   z=x.split(';')
#   lplz2.append([z[0],z[1],z[2],z[3],int(z[4])])
   

#lf=[]
#lf_s=[]
#for x in lplz2:
   #print x[4]
#   nr=x[4]
#   r=[]
#   for v in gn1:
#        print nr,v[0]
#        if nr==v[0]:
#	    r.append(v)
#   lf.append([x[0],x[1],x[2],x[3],r])
#   lf_s.append(x[0]+';'+x[1]+';'+x[2]+';'+x[3]+';'+str(r)+';'+';\r\n')
     
#ff=open('lf.txt','w+')
#ff.writelines(lf_s)
#ff.close()