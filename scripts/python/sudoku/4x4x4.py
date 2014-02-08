# coding=UTF-8
# fonction recursives pour tourver les permutations d un ensemble


def isSudoku(sudokuNumber, sudokuList, permutationList):
 ret=True
 allLines=sudokuList[sudokuNumber]
 # creer le modele
 modell=[]
 for x in allLines:
  modell.extend(permutationList[x])
 # tester les colones
 col1=[modell[0],modell[4],modell[8],modell[12]]
 col2=[modell[1],modell[5],modell[9],modell[13]]
 col3=[modell[2],modell[6],modell[10],modell[14]]
 col4=[modell[3],modell[7],modell[11],modell[15]]
 if not col1 in permutationList:
  ret=False
 if not col2 in permutationList:
  ret=False
 if not col3 in permutationList:
  ret=False
 if not col4 in permutationList:
  ret=False
 if ret:
   if col1==col2 or col1==col3 or col1==col4:
    ret=false
   if col2==col3 or col2==col4 or col2==col1:
    ret=false
   if col3==col1 or col3==col2 or col3==col4:
    ret=false
   if col4==col1 or col4==col2 or col4==col3:
    ret=false
 # tester les cellules
 if ret:
  if not [modell[0],modell[1],modell[4],modell[5]] in permutationList:
   ret=False
  if not [modell[2],modell[3],modell[6],modell[7]] in permutationList:
   ret=False
  if not [modell[8],modell[9 ],modell[12],modell[13]] in permutationList:
   ret=False
  if not [modell[10],modell[11],modell[14],modell[15]] in permutationList:
   ret=False
 return ret


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

# initialisation 
set=[1,2,3,4]
allPermutations=findAllPermutations(set)
allPermutationsDict={}
permut=0
for x in allPermutations:
 allPermutationsDict[permut]=x
 permut+=1
 #print x
allSudokus=findAllPermutations(allPermutationsDict.keys(),20)
allSudokusDict={}
permut=0
for x in allSudokus:
 allSudokusDict[permut]=x
 permut+=1
 #print x

count=1
for x in allSudokusDict.keys():
 if isSudoku(x, allSudokusDict, allPermutations): 
  print str(count)+". grille numero "+str(x)
  for z in allSudokusDict[x]:
   print str(allPermutationsDict[z])
  print "---------------------------------"
  count+=1

print "nombre de grilles generees : "+str(len(allSudokusDict))


