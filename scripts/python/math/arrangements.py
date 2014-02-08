# coding=UTF-8

def arrays(set):
 """
 trouve l'ensemble des arrangements d'un ensemble
 	
 """
 ret=[set]
 return ret

def limitedArrays(set, length=1):
 """
 trouve l'ensemble des arrangements d'une certaine longueur d'un ensemble
 	
 si l est la longueur de l'ensemble de base
 si n est la longueur de l'arrangement
 alors il y a l!/(l-n)! arrangements de l'ensemble
 """
 ret=[]
 if length>len(set):
  length=len(set)
 if length<1:
  length=1
 if length>1:
  for x in set:
   subset=[]
   subset.extend(set)
   found=False
   for z in set:
    if not found:
     subset.remove(z)
    if z==x:
     found=True
   arrange=limitedArrays(subset, length-1)
   for z in arrange:
    if len(z)==length-1:
     line=[x]
     line.extend(z)
     ret.append(line)
 else:
  for x in set:
   ret.append([x])  
 return ret


set=range(1,46)
test=arrays(set)
print arrays.__doc__
print ""
print len(test), test
print ""
print "-----------------------------------------------------------------"
print ""
test=limitedArrays(set, 5)
print limitedArrays.__doc__
print ""
print len(test), test





