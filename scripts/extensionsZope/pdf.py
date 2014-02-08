#####################################################################
#   code for the transformation in a pdf document using htmldoc     #
#       report your questions to jeantinguelyawais @ gmail.com      #
#                      year created : 2006                          #
#####################################################################

import os

# 1cm = 28 px
path_index="/home/zope/instances/gastro-plus/var/index.txt"
path_htmldoc="/usr/bin/htmldoc"
path="/home/zope/instances/gastro-plus/var/mediafolder/"
#options=" --size A4 -- bottom 43 --top 43 --right 43 --left 43 --no-title --jpeg=100 --footer ... --header ... "
options=" --size A4 --bottom 43 --top 43 --right 43 --left 43 --no-title --jpeg=100 --footer ... --header ... "
html_header_p="<html><head></head><body><center><table width=80%  height=730 halign=middle ><tr valign=middle><td> "
html_header_l="<html><head></head><body><center><table width=98% border=1 cellspacing=91 cellpadding=5  height=480 ><tr valign=middle><td width=49%> "
html_beetween_l="<br><hr width=100%><p align=center>www.gastro-plus.ch - Das Suchportal f&uuml;r Geniesser</p></td><td width=49%> "
html_footer_p="<br><hr width=100%><p align=center>www.gastro-plus.ch - Das Suchportal f&uuml;r Geniesser</p></td></tr><tr></tr></table></body></html>"
html_footer_l=" <br><hr width=100%><p align=center>www.gastro-plus.ch - Das Suchportal f&uuml;r Geniesser</p></td></tr></table></body></html>"

def webpage2pdf_portrait(what_in):
	mes1= "OK!"
	mes2= "<br>htmldoc : "
	my_index=file(path_index,'r+')
	try:
	    val=int(my_index.read())
	except:
	   val=0
	my_index.close()
	mes1=mes1+' '+str(val)+' : '
	my_file=file(path+str(val)+'.html','w+')
	my_file.write(html_header_p+what_in+html_footer_p)
	my_file.close()
	val=val+1
	my_index=file(path_index,'w+')
	my_index.write(str(val))
	my_index.close
	cmd=path_htmldoc+' --webpage'+options+'-f '+path+str(val-1)+'.pdf '+path+str(val-1)+'.html '
	mes2=mes2+os.popen(cmd+" 2>&1 3>&1").read()
	return str(val-1)
	

def webpage2pdf_landscape(what_in):
	mes1= "OK!"
	mes2= "<br>htmldoc : "
	my_index=file(path_index,'r+')
	try:
	    val=int(my_index.read())
	except:
	   val=0
	my_index.close()
	mes1=mes1+' '+str(val)+' : '
	my_file=file(path+str(val)+'.html','w+')
	my_file.write(html_header_l+what_in+html_beetween_l+what_in+html_footer_p)
	my_file.close()
	val=val+1
	my_index=file(path_index,'w+')
	my_index.write(str(val))
	my_index.close
	cmd=path_htmldoc+' --webpage --landscape'+options+'-f '+path+str(val-1)+'.pdf '+path+str(val-1)+'.html ' 
	mes2=mes2+os.popen(cmd+" 2>&1 3>&1").read()
	return str(val-1)
