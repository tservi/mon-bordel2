import os, sys
import Image

dir = 'C:/Users/jean/Desktop/atelier_nature_mai_2009'
size = 600, 600

def resizeImage ( files ):
    for file in files:
    	    outfile = 'miniature_' + file
	    if file != outfile:
	        try:
	            im = Image.open(	file )
	            im.thumbnail(   	size )
	            im.save( outfile , "JPEG")
		    print 'Image created : ' + outfile +'\n'
	        except IOError:
	            print "cannot create thumbnail for", infile

os.chdir ( dir )
# print os.getcwd ( )
files = os.listdir ( os.getcwd ( ) )
resizeImage ( files )