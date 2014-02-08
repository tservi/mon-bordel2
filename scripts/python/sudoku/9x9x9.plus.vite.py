# coding=UTF-8
# trouver toutes les grilles pleines aptes à donner des sudokus

import math

class gridModell(object):
 def __init__(self,set=[]):
  self.set=set
  self.sqrt=math.sqrt(len(set))
  self.len=len(set)
  model=[]
  for x in set:
   line=[]
   for z in set:
    line.append(0)
   model.append(line)
  self.model=model
  
  def getSqrt(self):
   return self.sqrt

  def getLen(self):
   return self.len  

 def fill(self,value,position):
  line=int(position/len(self.set))
  col=position-line*len(self.set)
  self.model[line][col]=value

 def string(self):
  return str(self.model)

 def getModel(self):
  return self.model

class SudokuGrid(object):
 def __init__(self,set=[]):
  self.model=gridModell(set)

 def getModel(self,val=''):
  return self.model
 



def findAllPermutations( set ,length=1):
 # fonction recursive
 ret=[set[0:len(set)-length+1]]
 if len(set)>length:
  ret=[]
  for x in set:
   subset = []
   subset.extend( set )
   subset.remove( x )
   permut = findAllPermutations( subset ,length)
   #print permut 
   for z in permut:
    line=[x]
    line.extend(z)
    ret.append(line)
 return ret

set=[1,2,3,4]
permutations=findAllPermutations(set)
mySudoku=SudokuGrid(set)
mySudoku.getModel().fill(1,0)
print mySudoku.getModel().string()



