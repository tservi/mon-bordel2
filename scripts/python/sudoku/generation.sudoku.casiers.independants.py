# coding=UTF-8
# génération des grilles du sudoku par casiers indépendants

import math

class gridModell(object):

 def __init__(self,set=[]):
  modell=[]
  for x in set:
   line=[]
   for z in set:
    line.append(0)
   modell.append(line)
  self.modell=modell
  
  
 def fill(self,value,position):
  ret=True
  line=int(position/len(self.modell))
  col=position-line*len(self.modell)
  if self.modell[line][col]==0:
   self.modell[line][col]=value
  else:
   ret=False
  return ret

 def string(self):
  return str(self.modell)

 def getModell(self):
  return self.modell

 def toString(self):
  ret=''
  sqrt=math.sqrt(len(self.modell))
  colIndex=0
  for x in self.modell:
   lineIndex=0
   for z in x :
    ret+=str(z)+' '
    if lineIndex%(sqrt)==sqrt-1:
      ret+='| '
    lineIndex+=1
   ret+='\n'
   if colIndex%sqrt==sqrt-1:
    for do in range(0, int(len(self.modell)+sqrt)):
     ret+='--'
    ret+='\n'
   colIndex+=1
  return ret 


class sudokuGridModell(object):

 def __init__(self,set=[]):
  modells={}
  for x in set:
   modells[x]=gridModell(set)
  modells['total']=gridModell(set)
  self.modells=modells
  self.set=set

 def testAndFill(self,value,position):
  ret=True
  myLen=len(self.modells.keys())-1
  sqrt=int(math.sqrt(myLen))
  if position in range(0, myLen*myLen):
   line=int(position/myLen)
   col=position-line*myLen
   #test=True
   #if not(self.modells.has_key(value) and self.modells[value].modell[line][col]==0):
   #  test=False
   #if self.modells['total'].modell[line][col]>0:
   #  test=False
   test=self.isPossible(value, position)
   ret=test
   if test:
    self.modells['total'].modell[line][col]=value
    for nc in range(0,myLen):
     self.modells[value].modell[line][nc]=value
    for nl in range(0,myLen):
     self.modells[value].modell[nl][col]=value
    # a controller
    # le nombre de colonnes = col + 1 
    # le nombre de lignes = line + 1  
    # l'intervales est de longueur sqrt
    # il y a myLen / sqrt intervalles possibles = sqrt intervales possibles 
    firstLine=int(col/sqrt)*sqrt
    lastLine=int(firstLine+sqrt)
    firstCol=int(line/sqrt)*sqrt
    lastCol=int(firstCol+sqrt)
    #print col, sqrt, nc, firstLine, lastLine
    #print line, sqrt, nl, firstCol, lastCol
    # 
    for nc in range(firstLine, lastLine):
     for nl in range(firstCol, lastCol):
      if nl<myLen and nc<myLen:
       self.modells[value].modell[nl][nc]=value
    for x in self.modells.keys():
     if x==value or x=='total':
      print self.modells[x].toString()   
  else:
   ret=False
  return ret
       
 def isPossible(self,value,position):
  ret=True
  myLen=len(self.modells.keys())-1
  sqrt=int(math.sqrt(myLen))
  if position in range(0, myLen*myLen):
   line=int(position/myLen)
   col=position-line*myLen
   if self.modells['total'].modell[line][col]>0 or not(self.modells.has_key(value) and self.modells[value].modell[line][col]==0):
    ret=False
  else:
   ret=False
  return ret 

 def fill(self,value,position):
  ret=True
  myLen=len(self.modells.keys())-1
  sqrt=int(math.sqrt(myLen))
  if position in range(0, myLen*myLen):
   line=int(position/myLen)
   col=position-line*myLen
   self.modells['total'].modell[line][col]=value
   for nc in range(0,myLen):
    self.modells[value].modell[line][nc]=value
   for nl in range(0,myLen):
    self.modells[value].modell[nl][col]=value
   firstLine=int(col/sqrt)*sqrt
   lastLine=int(firstLine+sqrt)
   firstCol=int(line/sqrt)*sqrt
   lastCol=int(firstCol+sqrt)
   for nc in range(firstLine, lastLine):
    for nl in range(firstCol, lastCol):
     #if nl<myLen and nc<myLen:
     self.modells[value].modell[nl][nc]=value
   #for x in self.modells.keys():
   # if x==value or x=='total':
   #  print self.modells[x].toString()   
  else:
   ret=False
  return ret


 def isFinished(self):
  ret=True
  for line in self.modells['total'].modell:
   for col in line:
    if col==0:
     ret=False
  return ret

 def restInLine(self, position):
  ret=[]
  ret.extend(self.set)
  myLen=len(self.modells.keys())-1
  sqrt=int(math.sqrt(myLen))
  if position in range(0, myLen*myLen):
   line=int(position/myLen)
   for val in self.modells['total'].modell[line]:
    if val in ret:
     ret.remove(val)
  return ret 

 def restInCol(self, position):
  ret=[]
  ret.extend(self.set)
  myLen=len(self.modells.keys())-1
  sqrt=int(math.sqrt(myLen))
  if position in range(0, myLen*myLen):
   line=int(position/myLen)
   col=position-line*myLen
   for newPosition in range(col,myLen*myLen, myLen):
    newLine=int(newPosition/myLen)
    newCol=newPosition-newLine*myLen
    val=self.modells['total'].modell[newLine][newCol]
    #print newPosition, newLine, newCol, val, ret
    if val in ret:
     ret.remove(val)
  return ret 

 def restInCell(self, position):
  ret=[]
  ret.extend(self.set)
  myLen=len(self.modells.keys())-1
  sqrt=int(math.sqrt(myLen))
  if position in range(0, myLen*myLen):
   line=int(position/myLen)
   col=position-line*myLen
   firstLine=int(col/sqrt)*sqrt
   lastLine=int(firstLine+sqrt)
   firstCol=int(line/sqrt)*sqrt
   lastCol=int(firstCol+sqrt)
   for nc in range(firstLine, lastLine):
    for nl in range(firstCol, lastCol):
     #if nl<myLen and nc<myLen:
     val=self.modells['total'].modell[nl][nc]
     #print newPosition, newLine, newCol, val, ret
     if val in ret:
      ret.remove(val)
  return ret 

 def restAtPosition(self, position):
  ret=[]
  myLen=len(self.modells.keys())-1
  sqrt=int(math.sqrt(myLen))
  if position in range(0, myLen*myLen):
   line=int(position/myLen)
   col=position-line*myLen
   if self.modells['total'].modell[line][col]==0: 
    for line in self.restInLine(position):
     for col in self.restInCol(position):
      for cell in self.restInCell(position):
       if line==col and line==cell:
        ret.append(line)
  return ret 

 def nextCase(self, position):
  ret=position
  return ret
 
 def restInCase(self, position):
  ret=postion
  return ret 


set=[1,2,3,4,5,6,7,8,9]
#set=[1,2,3,4]
myLen=int(len(set))
sqrt=int(math.sqrt(myLen))
newSudokuGrid=sudokuGridModell(set)
#filled={}
#newSudokuGrid.fill(set[0],0)
positionDone=[]
offset=int(0)
for x in range(0,int((myLen*myLen)+(sqrt*sqrt))):
 offset=int(x)
 step=int(offset/myLen)
 rest=int(offset%myLen)
 position=(x*myLen+step+rest)%(myLen*myLen)
 val=newSudokuGrid.restAtPosition(int(position))
 if len(val)>0:
  add=val[0]
  newSudokuGrid.fill(add,int(position))
  #print offset, step, rest, position, val[0]
  positionDone.append(position) 
 else:
  print ".......... why ????"
 #offset+=int(sqrt)
 #offset+=int(1)
print positionDone
print newSudokuGrid.modells['total'].toString()
#newSudokuGrid=sudokuGridModell(set)
#positionDone=[]
#offset=int(0)
#for x in range(0,int(myLen*myLen)):
# #offset=int(x)
# step=int(offset/myLen)
# rest=int(offset%myLen)
# position=(x*myLen+step+rest)%(myLen*myLen)
# val=newSudokuGrid.restAtPosition(int(position))
# if len(val)>0:
#  add=val[0]
#  newSudokuGrid.fill(add,int(position))
#  print x, offset, position, val[0]
#  positionDone.append(position) 
# else:
#  print ".......... why ????"
# offset+=int(sqrt)
# #offset+=int(1)
#print positionDone
#print newSudokuGrid.modells['total'].toString()
