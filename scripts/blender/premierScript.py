# api de blender : http://www.blender.org/documentation/248PythonDoc/
# un petit exemple : http://jmsoler.free.fr/didacticiel/blender/tutor/python_script01.htm
# lexique pratique : http://jmsoler.free.fr/lexique1.htm
# premier script test -- ce script est uniquement un petit test avec la version 2.4.5 de blender

import Blender
import sys

# mettre un petit message dans la console 
obj=Blender.Object.Get()
print ''
print '-------------------------------------------------'
print 'Hello : '+str(obj)

# ajouter un mesh (dans ce cas un carre)
from Blender import NMesh
me= NMesh.GetRaw()                    # insertion du mesh 
print str(me.__methods__)             # voir les methodes contenues dans l'objet
v=NMesh.Vert(1.0,0.0,0.0)             # creation d'un sommet
print 'avant : '+str(me.verts)
me.verts.append(v)                    # ajout du sommet a la liste des sommets de l'objet 
v=NMesh.Vert(1.0,1.0,0.0)
me.verts.append(v)
v=NMesh.Vert(0.0,1.0,0.0)
me.verts.append(v)
v=NMesh.Vert(0.0,0.0,0.0)
me.verts.append(v)
print 'apres : '+str(me.verts)
f=NMesh.Face()                        # creation de l'objet facettes
f.v.append(me.verts[0])               # association des facettes et des sommets
f.v.append(me.verts[1])
f.v.append(me.verts[2])
f.v.append(me.verts[3])
me.faces.append(f)                    # association de l'objet f avec les faces du mesh 
NMesh.PutRaw(me,"plane",1)            # ajout de l'objet dans Blender
Blender.Redraw()                      # mise à jour de Blender 

