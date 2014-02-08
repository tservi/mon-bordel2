import Blender
from Blender import Text3d, Scene, Material, NMesh, Object

found=False
myF=None
for k in Text3d.Font.Get():
	if k.name=='t-servi.ttf':
		myF=k
		found=True
		print "already found!"

if not found:
	myF=Text3d.Font.Load('t-servi.ttf')
	print "font installed"

found=False
vert=None
for k in Material.Get():
	if k.name=='vert':
		vert=k
		found=True
		print "already found!"

if not found:		
	vert=Material.New('vert')
	vert.setAlpha(0.65)
	#vert.setRGBCol(0.0,1.0,0.0)
	vert.rgbCol = [0.0,1.0,0.0]


myT=Text3d.New("myT")
myT.setText("t-servi.com")
myT.setExtrudeDepth(0.10)
myT.setExtrudeBevelDepth(0.06)
myT.setDrawMode(Text3d.DRAWFRONT)

if myF is not None:
	myT.setFont(myF)


ob = Object.New('Text')
ob.link(myT)

txtv = NMesh.GetRawFromObject(ob.name)
tob = Object.New('Mesh','MyObj')
tob.link(txtv)

[x,y,z] = tob.getSize()
print "Width: ", x, " Height: ", y
tob.setMaterials([vert])
tob.colbits = (1<<0)
Scene.GetCurrent().objects.link(tob)

#scn = Scene.GetCurrent()
#ob = scn.objects.new(myT)
#ob.makeDisplayList()
Blender.Window.RedrawAll()