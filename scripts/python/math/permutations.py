# coding=UTF-8
# 

def allPermutations(set):
 """ 
  fonction recursive, trouve l'ensemble des permutations d'un ensemble 
  si n est le nobre d'éléments de l'ensemble alors l'ensemble des permutations
  a une logueur de n!
 """
 ret=[set] 
 if len(set)>1:
  ret=[]
  for x in set:
   subset = []
   subset.extend( set )
   subset.remove( x )
   permut = allPermutations(subset)
   for z in permut:
    line=[x]
    line.extend(z)
    ret.append(line)
 return ret

def findAllPermutations( set ,length=1):
 """
 fonction recursive, trouve l'ensemble des permutations d'une certaine longueur
 dans un ensemble
 si n est le nombre d'éléments de l'ensemble et p la longeur voulue alors 
 l'ensemble des permutations a une valeur de n!/(n-p)!
 remarque : dans le cas ou p=n-1 => n!/(n-n+1)! = n!/1! = n!
 """
 #print set, length
 ret=[] 
 if length>len(set):
  length=len(set)
 if length<1:
  length=1
 if length>1:
  ret=[]
  for x in set:
   subset = []
   subset.extend( set )
   subset.remove( x )
   permut = findAllPermutations(subset,length-1)
   for z in permut:
    line=[x]
    line.extend(z)
    ret.append(line)
 else:
  for x in set:
   ret.append([x])
 return ret

set=[1,2,3,4]
test=allPermutations(set)
print allPermutations.__doc__
print ""
print len(test), test
print ""
print "-----------------------------------------------------------------"
print ""
test=findAllPermutations(set, len(set)-2)
print len(test), test
print findAllPermutations.__doc__


