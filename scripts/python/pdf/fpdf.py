# coding=UTF-8
#/*******************************************************************************
#* FPDF                                                                         *
#*                                                                              *
#* Version : 1.6                                                                *
#* Date :    2008-08-03                                                         *
#* Auteur :  Olivier PLATHEY                                                    *
#*******************************************************************************/
# port of fpdf : http://www.fpdf.org
# state : experimental
# done by Jean Tinguely Awais
# http://www.t-servi.com
#
# !!! 	there is already 2 ports of fpdf in python  !!!
# !!! 	http://www.fpdf.org/dl.php?id=94	    !!!	
# !!! 	http://juanfernandoe.googlepages.com/	    !!!
# !!! 	Please use one of this instead of my port   !!! 	
#

import sys 
from zlib import *
from datetime import *

# the font directory comes from http://juanfernandoe.googlepages.com/
from font import fpdf_charwidths

FPDF_VERSION=1.6
fpdf_charwidths={}

class FPDF(object):
 """
Port of fpdf in python
/******************************************************************************
* FPDF                                                                        *
*                                                                             *
* Version : 1.6                                                               *
* Date :    2008-08-03                                                        *
* Auteur :  Olivier PLATHEY                                                   *
******************************************************************************/
port of fpdf : http://www.fpdf.org
done by Jean Tinguely Awais
http://www.t-servi.com

 """
 #	page               #current page number
 #	n                  #current object number
 #	offsets            #array of object offsets
 #	buffer             #buffer holding in-memory PDF
 #	pages              #array containing pages
 #	state              #current document state
 #	compress           #compression flag
 #	k                  #scale factor (number of points in user unit)
 #	 defOrientation     # default orientation
 #	CurOrientation     #current orientation
 # 	PageFormats        #available page formats
 #	 defPageFormat      # default page format
 #	CurPageFormat      #current page format
 #	PageSizes          #array storing non- default page sizes
 #	wPt
 #	hPt          	 #dimensions of current page in points
 #	w
 #	h               #dimensions of current page in user unit
 #	lMargin            #left margin
 #	tMargin            #top margin
 #	rMargin            #right margin
 #	bMargin            #page break margin
 #	cMargin            #cell margin
 #	x
 #	y               #current position in user unit
 #	lasth              #height of last printed cell
 #	LineWidth          #line width in user unit  #	CoreFonts          #array of standard font names
 #	fonts              #array of used fonts
 #	FontFiles          #array of font files
 #	diffs              #array of encoding differences
 #	FontFamily         #current font family
 #	FontStyle          #current font style
 #	underline          #underlining flag
 #	CurrentFont        #current font info
 #	FontSizePt         #current font size in points
 #	FontSize           #current font size in user unit
 #	DrawColor          #commands for drawing color
 #	FillColor          #commands for filling color
 #	TextColor          #commands for text color
 #	ColorFlag          #indicates whether fill and text colors are different
 #	ws                 #word spacing
 #	images             #array of used images
 #	PageLinks          #array of links in pages
 #	links              #array of internal links
 #	AutoPageBreak      #automatic page breaking
 #	PageBreakTrigger   #threshold used to trigger page breaks
 #	InHeader           #flag set when processing header
 #	InFooter           #flag set when processing footer
 #	ZoomMode           #zoom display mode
 #	LayoutMode         #layout display mode
 #	title              #title
 #	subject            #subject
 #	author             #author
 #	keywords           #keywords
 #	creator            #creator
 #	AliasNbPages       #alias for total number of pages
 #	PDFVersion         #PDF version number

 def __init__(self,orientation='P', unit='mm', format='A4'):
	self.fpdfTranslator='http://www.t-servi.com'
	# !!! I take this code from http://juanfernandoe.googlepages.com/ !!!
     	#Private properties
     	self.page=None;               #current page number
     	self.n=None;                  #current object number
     	self.offsets={}; #python: array() => {}            #array of object offsets
     	self.buffer=None;             #buffer holding in-memory PDF
     	self.pages=None;              #array containing pages
     	self.state=None;              #current document state
     	self.compress=None;           #compression flag
     	self.DefOrientation=None;     #default orientation
     	self.CurOrientation=None;     #current orientation
     	self.OrientationChanges=None; #array indicating orientation changes
     	self.k=None;                  #scale factor (number of points in user unit)
     	self.fwPt=None; self.fhPt=None;         #dimensions of page format in points
     	self.fw=None; self.fh=None;             #dimensions of page format in user unit
     	self.wPt=None; self.hPt=None;           #current dimensions of page in points
     	self.w=None; self.h=None;               #current dimensions of page in user unit
     	self.lMargin=None;            #left margin
     	self.tMargin=None;            #top margin
     	self.rMargin=None;            #right margin
     	self.bMargin=None;            #page break margin
     	self.cMargin=None;            #cell margin
     	self.x=None; self.y=None;               #current position in user unit for cell positioning
     	self.lasth=None;              #height of last cell printed
     	self.LineWidth=None;          #line width in user unit
     	self.CoreFonts=None;          #array of standard font names
     	self.fonts={};              #array of used fonts
     	self.FontFiles=None;          #array of font files
     	self.diffs=None;              #array of encoding differences
     	self.images={};             #array of used images
     	self.PageLinks={}; #python: array() => {}          #array of links in pages
     	self.links=None;              #array of internal links
     	self.FontFamily=None;         #current font family
     	self.FontStyle='';          #current font style
     	self.underline=None;          #underlining flag
     	self.CurrentFont=None;        #current font info
     	self.FontSizePt=None;         #current font size in points
     	self.FontSize=None;           #current font size in user unit
     	self.DrawColor=None;          #commands for drawing color
     	self.FillColor=None;          #commands for filling color
     	self.TextColor=None;          #commands for text color
     	self.ColorFlag=None;          #indicates whether fill and text colors are different
     	self.ws=None;                 #word spacing
     	self.AutoPageBreak=None;      #automatic page breaking
     	self.PageBreakTrigger=None;   #threshold used to trigger page breaks
     	self.InFooter=None;           #flag set when processing footer
     	self.ZoomMode=None;           #zoom display mode
     	self.LayoutMode=None;         #layout display mode
     	self.title=None;              #title
     	self.subject=None;            #subject
     	self.author=None;             #author
     	self.keywords=None;           #keywords
     	self.creator=None;            #creator
     	#self.AliasNbPages=None;      #alias for total number of pages 
     	self.PDFVersion=None;         #PDF version number
	# !!! end of code !!!
	#Some checks
	self.__dochecks__()
	#Initialization of properties
	self.page=0
	self.n=2
	self.buffer=''
	self.pages={}
	self.PageSizes={}
	self.state=0
	self.fonts={}
	self.FontFiles={}
	self.diffs={}
	self.images={}
	self.links={}
	self.InHeader=False
	self.InFooter=False
	self.lasth=0
	self.FontFamily=''
	self.FontStyle=''
	self.FontSizePt=12
	self.underline=False
	self.DrawColor='0 G'
	self.FillColor='0 g'
	self.TextColor='0 g'
	self.ColorFlag=False
	self.ws=0
	#Standard fonts
	self.CoreFonts={'courier':'Courier', 'courierB':'Courier-Bold', 'courierI':'Courier-Oblique', 'courierBI':'Courier-BoldOblique',
		'helvetica':'Helvetica', 'helveticaB':'Helvetica-Bold', 'helveticaI':'Helvetica-Oblique', 'helveticaBI':'Helvetica-BoldOblique',
		'times':'Times-Roman', 'timesB':'Times-Bold', 'timesI':'Times-Italic', 'timesBI':'Times-BoldItalic',
		'symbol':'Symbol', 'zapfdingbats':'ZapfDingbats'}
	#Scale factor
	if(unit=='pt'):
		self.k=1
	elif(unit=='mm'):
		self.k=72/25.4
	elif(unit=='cm'):
		self.k=72/2.54
	elif(unit=='in'):
		self.k=72
	else:
		self.Error('Incorrect unit: '.unit)
	#Page format
	self.PageFormats={'a3':[841.89,1190.55], 'a4':[595.28,841.89], 'a5':[420.94,595.28],
		'letter':[612,792], 'legal':[612,1008]}
	if(isinstance(format, str)):
		format=self.__getpageformat__(format)
	self. defPageFormat=format
	self.CurPageFormat=format
	#Page orientation
	orientation=str(orientation).lower()
	if(orientation=='p' or orientation=='portrait'):
		self. defOrientation='P'
		self.w=self. defPageFormat[0]
		self.h=self. defPageFormat[1]
	elif(orientation=='l' or orientation=='landscape'):
		self. defOrientation='L'
		self.w=self. defPageFormat[1]
		self.h=self. defPageFormat[0]
	else:
		self.Error('Incorrect orientation: '.orientation)
	self.CurOrientation=self. defOrientation
	self.wPt=self.w*self.k
	self.hPt=self.h*self.k
	#Page margins (1 cm)
	margin=28.35/self.k
	self.SetMargins(margin,margin)
	#Interior cell margin (1 mm)
	self.cMargin=margin/10
	#Line width (0.2 mm)
	self.LineWidth=.567/self.k
	#Automatic page break
	self.SetAutoPageBreak(True,2*margin)
	#Full width display mode
	self.SetDisplayMode('fullwidth')
	#Enable compression
	self.SetCompression(False)
	#self.SetCompression(True)
	#Set  default PDF version number
	self.PDFVersion='1.3'


 #/*******************************************************************************
 #*                                                                              *
 #*                               Public methods                                 *
 #*                                                                              *
 #*******************************************************************************/
 def SetMargins(self,left, top, right=None):
	#Set left, top and right margins
	self.lMargin=left
	self.tMargin=top
	if(right is None):
		right=left
	self.rMargin=right

 def SetLeftMargin(self,margin):
	#Set left margin
	self.lMargin=margin
	if(self.page>0 and self.x<margin):
		self.x=margin

 def SetTopMargin(self,margin):
	#Set top margin
	self.tMargin=margin

 def SetRightMargin(self,margin):
	#Set right margin
	self.rMargin=margin

 def SetAutoPageBreak(self,auto, margin=0):
	#Set auto page break mode and triggering margin
	self.AutoPageBreak=auto
	self.bMargin=margin
	self.PageBreakTrigger=self.h-margin


 def SetDisplayMode(self,zoom, layout='continuous'):
	#Set display mode in viewer
	if(zoom=='fullpage' or zoom=='fullwidth' or zoom=='real' or zoom==' default' or not isinstance(zoom,str)):
		self.ZoomMode=zoom
	else:
		self.Error('Incorrect zoom display mode: '.zoom)
	if(layout=='single' or layout=='continuous' or layout=='two' or layout==' default'):
		self.LayoutMode=layout
	else:
		self.Error('Incorrect layout display mode: '.layout)

 def SetCompression(self,compress):
	#Set page compression
	if( sys.modules.has_key('zlib')):
		self.compress=compress
	else:
		self.compress=False

 def SetTitle(self,title, isUTF8=False):
	#Title of document
	if(isUTF8):
		title=self.__UTF8toUTF16__(title)
	self.title=title


 def SetSubject(self,subject, isUTF8=False):
	#Subject of document
	if(isUTF8):
		subject=self.__UTF8toUTF16__(subject)
	self.subject=subject

 def SetAuthor(self,author, isUTF8=False):
	#Author of document
	if(isUTF8):
		author=self.__UTF8toUTF16__(author)
	self.author=author

 def SetKeywords(self,keywords, isUTF8=False):
	#Keywords of document
	if(isUTF8):
		keywords=self.__UTF8toUTF16__(keywords)
	self.keywords=keywords

 def SetCreator(self,creator, isUTF8=False):
	#Creator of document
	if(isUTF8):
		creator=self.__UTF8toUTF16__(creator)
	self.creator=creator

 def AliasNbPages(self,alias='{nb}'):
	# define an alias for total number of pages
	#self.AliasNbPages=alias
	return alias

 def Error(self,msg):
	#Fatal error
	raise '<b>FPDF error:</b> '+msg


 def Open(self):
	#Begin document
	self.state=1

 def Close(self):
	#Terminate document
	if(self.state==3):
		return
	if(self.page==0):
		self.AddPage()
	#Page footer
	self.InFooter=True
	self.Footer()
	self.InFooter=False
	#Close page
	self.__endpage__()
	#Close document
	self.__enddoc__()


 def AddPage(self,orientation='', format=''):
	"#Start a new page"
	if(self.state==0):
		self.Open()
	family=self.FontFamily
	style=self.FontStyle
	if self.underline:
 		style=style+'U'
	size=self.FontSizePt
	lw=self.LineWidth
	dc=self.DrawColor
	fc=self.FillColor
	tc=self.TextColor
	cf=self.ColorFlag
	if(self.page>0):
		#Page footer
		self.InFooter=True
		self.Footer()
		self.InFooter=False
		#Close page
		self.__endpage__()
	#Start new page
	self.__beginpage__(orientation,format)
	#Set line cap style to square
	self.__out__('2 J')
	#Set line width
	self.LineWidth=lw
	self.__out__('%.2F w'%(lw*self.k))
	#Set font
	if(family):
		self.SetFont(family,style,size)
	#Set colors
	self.DrawColor=dc
	if(not dc=='0 G'):
		self.__out__(dc)
	self.FillColor=fc
	if(not fc=='0 g'):
		self.__out__(fc)
	self.TextColor=tc
	self.ColorFlag=cf
	#Page header
	self.InHeader=True
	self.Header()
	self.InHeader=False
	#Restore line width
	if(not self.LineWidth==lw):
		self.LineWidth=lw
		self.__out__('%.2F w'%(lw*self.k))
	#Restore font
	if(family):
		self.SetFont(family,style,size)
	#Restore colors
	if(not self.DrawColor==dc):
		self.DrawColor=dc
		self.__out__(dc)
	if(not self.FillColor==fc):
		self.FillColor=fc
		self.__out__(fc)
	self.TextColor=tc
	self.ColorFlag=cf

 def Header(self):
	#To be implemented in your own inherited class
        pass

 def Footer(self):
	#To be implemented in your own inherited class
	pass


 def PageNo(self):
	#Get current page number
	return self.page


 def SetDrawColor(self,r, g=None, b=None):
	#Set color for all stroking operations
	if((r==0 and g==0 and b==0) or g is None):
		self.DrawColor='%.3F G'%(r/255)
	else:
		self.DrawColor='%.3F %.3F %.3F RG'%(r/255,g/255,b/255)
	if(self.page>0):
		self.__out__(self.DrawColor)


 def SetFillColor(self,r, g=None, b=None):
	#Set color for all filling operations
	if((r==0 and g==0 and b==0) or g is None):
		self.FillColor='%.3F g'%(r/255)
	else:
		self.FillColor='%.3F %.3F %.3F rg'%(r/255,g/255,b/255)
	self.ColorFlag=(self.FillColor!=self.TextColor)
	if(self.page>0):
		self.__out__(self.FillColor)

 def SetTextColor(self,r, g=None, b=None):
	#Set color for text
	if((r==0 and g==0 and b==0) or g is None):
		self.TextColor='%.3F g'%(r/255)
	else:
		self.TextColor='%.3F %.3F %.3F rg'%(r/255,g/255,b/255)
	self.ColorFlag=(self.FillColor!=self.TextColor)

 def GetStringWidth(self,s):
	#Get width of a string in the current font
	s=str(s)
	cw=self.CurrentFont['cw']
	w=0
	l=len(s)
	for i in range(0,l):
		w+=cw[s[i]]
	return w*self.FontSize/1000

 def SetLineWidth(self,width):
	#Set line width
	self.LineWidth=width
	if(self.page>0):
		self.__out__('%.2F w'%(width*self.k))

 def Line(self,x1, y1, x2, y2):
	#Draw a line
	self.__out__('%.2F %.2F m %.2F %.2F l S'%(x1*self.k,(self.h-y1)*self.k,x2*self.k,(self.h-y2)*self.k))
	 
 def Rect(self,x, y, w, h, style=''):
	#Draw a rectangle
	if(style=='F'):
		op='f'
	elif(style=='FD' or style=='DF'):
		op='B'
	else:
		op='S'
	self.__out__('%.2F %.2F %.2F %.2F re %s'%(x*self.k,(self.h-y)*self.k,w*self.k,-h*self.k,op))


 def AddFont(self,family, style='', file=''):
	#Add a TrueType or Type1 font
        # a tester 
	family=str(family).lower()
	if(file==''):
		file=family.replace(' ','')+style.lower()+'.py'
	if(family=='arial'):
		family='helvetica'
	style=style.upper()
	if(style=='IB'):
		style='BI'
	fontkey=family+style
	if(self.fonts.has_key(fontkey)):
		return
        path=self.__getfontpatht__()
	exec('from '+path+file+' import * ')                  
	if( not name):
		self.Error('Could not include font  definition file')
	i=count(self.fonts)+1
	self.fonts[fontkey]={'i':i, 'type':type, 'name':name, 'desc':desc, 'up':up, 'ut':ut, 'cw':cw, 'enc':enc, 'file':file}
	if(diff):
		#Search existing encodings
		d=0
		nb=count(self.diffs)
		for i in range(1, nb+1):
			if(self.diffs[i]==diff):
				d=i
				break
		if(d==0):
			d=nb+1
			self.diffs[d]=diff
		self.fonts[fontkey]['diff']=d
	if(file):
		if(type=='TrueType'):
			self.FontFiles[file]={'length1':originalsize}
		else:
			self.FontFiles[file]={'length1':size1, 'length2':size2}

 def SetFont(self,family, style='', size=0):
	#Select a font size given in points
	# a tester
	#global fpdf_charwidths
	size=int(size)
	family=str(family).lower()
	if(family==''):
		family=self.FontFamily
	if(family=='arial'):
		family='helvetica'
	elif(family=='symbol' or family=='zapfdingbats'):
		style=''
	style=style.upper()
	if(style.find('U')>=0):
		self.underline=True
		style=style.replace('U','')
	else:
		self.underline=False
	if(style=='IB'):
		style='BI'
	if(size==0):
		size=self.FontSizePt
	#Test if font is already selected
	if(self.FontFamily==family and self.FontStyle==style and self.FontSizePt==size):
		return
	#Test if used for the first time
	fontkey=family+style
	if not self.fonts.has_key(fontkey):
		#Check if one of the standard fonts
		if(self.CoreFonts.has_key(fontkey)):
			if(not fpdf_charwidths.has_key(fontkey)):
				#Load metric file
				file=family
				if(family=='times' or family=='helvetica'):
					file+=style.lower()
                                path=self.__getfontpatht__()
				exec('from '+path+file+' import * ')
				if( not fpdf_charwidths.has_key(fontkey)):
					self.Error('Could not include font metric file')
			i=len(self.fonts)+1
			name=self.CoreFonts[fontkey]
			cw=fpdf_charwidths[fontkey]
			self.fonts[fontkey]={'i':i, 'type':'core', 'name':name, 'up':-100, 'ut':50, 'cw':cw}
		else:
			self.Error('Un defined font: '+family+' '+style)
	#Select it
	self.FontFamily=family
	self.FontStyle=style
	self.FontSizePt=size
	self.FontSize=size/self.k
	self.CurrentFont=self.fonts[fontkey]
	if(self.page>0):
		self.__out__('BT /F%d %.2F Tf ET'%(self.CurrentFont['i'],self.FontSizePt))

 def SetFontSize(self,size):
	#Set font size in points
	if(self.FontSizePt==size):
		return
	self.FontSizePt=size
	self.FontSize=size/self.k
	if(self.page>0):
		self.__out__('BT /F%d %.2F Tf ET'%(self.CurrentFont['i'],self.FontSizePt))

 def AddLink(self):
	#Create a new internal link
	n=count(self.links)+1
	self.links[n]=array(0, 0)
	return n


 def SetLink(self,link, y=0, page=-1):
	#Set destination of internal link
	if(y==-1):
		y=self.y
	if(page==-1):
		page=self.page
	self.links[link]=array(page, y)

 def Link(self,x, y, w, h, link):
	#Put a link on the page
	self.PageLinks[self.page].append([x*self.k, self.hPt-y*self.k, w*self.k, h*self.k, link])

 def Text(self,x, y, txt):
	#Output a string
	s='BT %.2F %.2F Td (%s) Tj ET'%(x*self.k,(self.h-y)*self.k,self.__escape__(txt))
	if(self.underline and not txt==''):
		s+=' '+self.__dounderline__(x,y,txt)
	if(self.ColorFlag):
		s='q '+self.TextColor+' '+s+' Q'
	self.__out__(s)

 def AcceptPageBreak(self):
	#Accept automatic page break or not
	return self.AutoPageBreak

 def Cell(self,w, h=0, txt='', border=0, ln=0, align='', fill=False, link=''):
	#Output a cell
	k=self.k
	if(self.y+h>self.PageBreakTrigger and not self.InHeader and not self.InFooter and self.AcceptPageBreak()):
		#Automatic page break
		x=self.x
		ws=self.ws
		if(ws>0):
			self.ws=0
			self.__out__('0 Tw')
		self.AddPage(self.CurOrientation,self.CurPageFormat)
		self.x=x
		if(ws>0):
			self.ws=ws
			self.__out__('%.3F Tw'%(ws*k))
	if(w==0):
		w=self.w-self.rMargin-self.x
	s=''
	if(fill or border==1):
		if(fill):
			#op=(border==1) ? 'B' : 'f'
			if border==1:
				op='B'
			else:
				op='f'
		else:
			op='S'
		s='%.2F %.2F %.2F %.2F re %s '%(self.x*k,(self.h-self.y)*k,w*k,-h*k,op)
	if(isinstance(border,str)):
		x=self.x
		y=self.y
		if(border.find('L')>=0):
			s+='%.2F %.2F m %.2F %.2F l S '%(x*k,(self.h-y)*k,x*k,(self.h-(y+h))*k)
		if(border.find('T')>=0):
			s+='%.2F %.2F m %.2F %.2F l S '%(x*k,(self.h-y)*k,(x+w)*k,(self.h-y)*k)
		if(border.find('R')>=0):
			s+='%.2F %.2F m %.2F %.2F l S '%((x+w)*k,(self.h-y)*k,(x+w)*k,(self.h-(y+h))*k)
		if(border.find('B')>=0):
			s+='%.2F %.2F m %.2F %.2F l S '%(x*k,(self.h-(y+h))*k,(x+w)*k,(self.h-(y+h))*k)
	if(not txt==''):
		if(align=='R'):
			dx=w-self.cMargin-self.GetStringWidth(txt)
		elif(align=='C'):
			dx=(w-self.GetStringWidth(txt))/2
		else:
			dx=self.cMargin
		if(self.ColorFlag):
			s+='q '+self.TextColor+' '
		txt2=txt.replace(')','\\)').replace('(','\\(').replace('\\','\\\\')
		s+='BT %.2F %.2F Td (%s) Tj ET'%((self.x+dx)*k,(self.h-(self.y+.5*h+.3*self.FontSize))*k,txt2)
		if(self.underline):
			s+=' '+self.__dounderline__(self.x+dx,self.y+.5*h+.3*self.FontSize,txt)
		if(self.ColorFlag):
			s+=' Q'
		if(link):
			self.Link(self.x+dx,self.y+0.5*h-0.5*self.FontSize,self.GetStringWidth(txt),self.FontSize,link)
	if(s):
		self.__out__(s)
	self.lasth=h
	if(ln>0):
		#Go to next line
		self.y+=h
		if(ln==1):
			self.x=self.lMargin
	else:
		self.x+=w

 def MultiCell(self,w, h, txt, border=0, align='J', fill=False):
	#Output text with automatic or explicit line breaks
	cw=self.CurrentFont['cw']
	if(w==0):
		w=self.w-self.rMargin-self.x
	wmax=(w-2*self.cMargin)*1000/self.FontSize
	s=txt.replace('\n','')
	nb=len(s)
	if(nb>0 and s[nb-1]=="\n"):
		nb-=1
	b=0
	if(border):
		if(border==1):
			border='LTRB'
			b='LRT'
			b2='LR'
		else:
			b2=''
			if(border.find('L')>=0):
				b2+='L'
			if(border.find('R')>=0):
				b2+='R'
			#b=(strpos(border,'T')!==False) ? b2.'T' : b2
			b=b2
			if border.find('T')>=0:
				b+='T'	
	sep=-1
	i=0
	j=0
	l=0
	ns=0
	nl=1
	while(i<nb):
		#Get next character
		c=s[i]
		if(c=="\n"):
			#Explicit line break
			if(self.ws>0):
				self.ws=0
				self.__out__('0 Tw')
			self.Cell(w,h,substr(s,j,i-j),b,2,align,fill)
			i+=1
			sep=-1
			j=i
			l=0
			ns=0
			nl+=1
			if(border and nl==2):
				b=b2
			continue
		if(c==' '):
			sep=i
			ls=l
			ns+=1
		l+=cw[c]
		if(l>wmax):
			#Automatic line break
			if(sep==-1):
				if(i==j):
					i+=1
				if(self.ws>0):
					self.ws=0
					self.__out__('0 Tw')
				self.Cell(w,h,substr(s,j,i-j),b,2,align,fill)
			else:
				if(align=='J'):
					#self.ws=(ns>1) ? (wmax-ls)/1000*self.FontSize/(ns-1) : 0
					self.ws=0
					if ns>1:
						self.ws=(wmax-ls)/1000*self.FontSize/(ns-1)
					self.__out__('%.3F Tw'%(self.ws*self.k))
				self.Cell(w,h,substr(s,j,sep-j),b,2,align,fill)
				i=sep+1
			sep=-1
			j=i
			l=0
			ns=0
			nl+=1
			if(border and nl==2):
				b=b2
		else:
			i+=1
	#Last chunk
	if(self.ws>0):
		self.ws=0
		self.__out__('0 Tw')
	if(border and border.find('B')>=0):
		b+='B'
	self.Cell(w,h,substr(s,j,i-j),b,2,align,fill)
	self.x=self.lMargin

 def Write(self,h, txt, link=''):
	#Output text in flowing mode
	cw=self.CurrentFont['cw']
	w=self.w-self.rMargin-self.x
	wmax=(w-2*self.cMargin)*1000/self.FontSize
	s=txt.replace('\r','')
	nb=len(s)
	sep=-1
	i=0
	j=0
	l=0
	nl=1
	while(i<nb):
		#Get next character
		c=s[i]
		if(c=="\n"):
			#Explicit line break
			self.Cell(w,h,substr(s,j,i-j),0,2,'',0,link)
			i+=1
			sep=-1
			j=i
			l=0
			if(nl==1):
				self.x=self.lMargin
				w=self.w-self.rMargin-self.x
				wmax=(w-2*self.cMargin)*1000/self.FontSize
			nl+=1
			continue
		if(c==' '):
			sep=i
		l+=cw[c]
		if(l>wmax):
			#Automatic line break
			if(sep==-1):
				if(self.x>self.lMargin):
					#Move to next line
					self.x=self.lMargin
					self.y+=h
					w=self.w-self.rMargin-self.x
					wmax=(w-2*self.cMargin)*1000/self.FontSize
					i+=1
					nl+=1
					continue
				if(i==j):
					i+=1
				self.Cell(w,h,substr(s,j,i-j),0,2,'',0,link)
			else:
				self.Cell(w,h,substr(s,j,sep-j),0,2,'',0,link)
				i=sep+1
			sep=-1
			j=i
			l=0
			if(nl==1):
				self.x=self.lMargin
				w=self.w-self.rMargin-self.x
				wmax=(w-2*self.cMargin)*1000/self.FontSize
			nl+=1
		else:
			i+=1
	#Last chunk
	if(i!=j):
		self.Cell(l/1000*self.FontSize,h,substr(s,j),0,0,'',0,link)

 def Ln(self,h=None):
	#Line feed  default value is last cell height
	self.x=self.lMargin
	if(h is None):
		self.y+=self.lasth
	else:
		self.y+=h

 def Image(self,file, x=None, y=None, w=0, h=0, type='', link=''):
	#Put an image on the page
	# a tester 
	if(self.images.has_key(file)):
		#First use of this image, get info
		if(type==''):
			pos=file.find('.')
			if(pos<0):
				self.Error('Image file has no extension and no type was specified: '.file)
			type=file[pos+1:len(file)]
		type=strtolower(type)
		if(type=='jpeg'):
			type='jpg'
		mtd='_parse'.type
		if(not method_exists(this,mtd)):
			self.Error('Unsupported image type: '.type)
		info=self.mtd(file)
		info['i']=len(self.images)+1
		self.images[file]=info
	else:
		info=self.images[file]
	#Automatic width and height calculation if needed
	if(w==0 and h==0):
		#Put image at 72 dpi
		w=info['w']/self.k
		h=info['h']/self.k
	elif(w==0):
		w=h*info['w']/info['h']
	elif(h==0):
		h=w*info['h']/info['w']
	#Flowing mode
	if(y is None):
		if(self.y+h>self.PageBreakTrigger and not self.InHeader and not self.InFooter and self.AcceptPageBreak()):
			#Automatic page break
			x2=self.x
			self.AddPage(self.CurOrientation,self.CurPageFormat)
			self.x=x2
		y=self.y
		self.y+=h
	if(x is None):
		x=self.x
	self.__out__('q %.2F 0 0 %.2F %.2F %.2F cm /I%d Do Q'%(w*self.k,h*self.k,x*self.k,(self.h-(y+h))*self.k,info['i']))
	if(link):
		self.Link(x,y,w,h,link)


 def GetX(self):
	#Get x position
	return self.x

 def SetX(self,x):
	#Set x position
	if(x>=0):
		self.x=x
	else:
		self.x=self.w+x

 def GetY(self):
	#Get y position
	return self.y

 def SetY(self,y):
	#Set y position and reset x
	self.x=self.lMargin
	if(y>=0):
		self.y=y
	else:
		self.y=self.h+y

 def SetXY(self,x, y):
	#Set x and y positions
	self.SetY(y)
	self.SetX(x)

 def Output(self,name='', dest=''):
	#Output PDF to some destination
	# a tester
	if(self.state<3):
		self.Close()
	dest=dest.upper()
	if(dest==''):
		if(name==''):
			name='doc.pdf'
			dest='I'
		else:
			dest='F'
	if(dest=='I'):
			#Send to standard output
			if(ob_get_length()):
				self.Error('Some data has already been output, can\'t send PDF file')
			if(not php_sapi_name()=='cli'):
				#We send to a browser
				header('Content-Type: application/pdf')
				if(headers_sent()):
					self.Error('Some data has already been output, can\'t send PDF file')
				header('Content-Length: '+len(self.buffer))
				header('Content-Disposition: inline filename="'+name+'"')
				header('Cache-Control: private, max-age=0, must-revalidate')
				header('Pragma: public')
				ini_set('zlib.output_compression','0')
			print self.buffer
	elif(dest=='D'):
			#Download file
			if(ob_get_length()):
				self.Error('Some data has already been output, can\'t send PDF file')
			header('Content-Type: application/x-download')
			if(headers_sent()):
				self.Error('Some data has already been output, can\'t send PDF file')
			header('Content-Length: '+len(self.buffer))
			header('Content-Disposition: attachment filename="'+name+'"')
			header('Cache-Control: private, max-age=0, must-revalidate')
			header('Pragma: public')
			ini_set('zlib.output_compression','0')
			print self.buffer
	elif(dest=='F'):
			#Save to local file
			f=file(name,'w+')
			if(not f):
				self.Error('Unable to create output file: '+name)
			else:
				f.writelines(self.buffer)
				f.close()
	elif(dest=='S'):
			#Return as a string
			return self.buffer
	else:
			self.Error('Incorrect output destination: '+dest)
	#return ''


 #/*******************************************************************************
 #*                                                                              *
 #*                              Protected methods                               *
 #*                                                                              *
 #*******************************************************************************/
 def __dochecks__(self):
        """
	#Check availability of %F
	if(sprintf('%.1F',1.0)!='1.0')
		self.Error('This version of PHP is not supported')
	#Check mbstring overloading
	if(ini_get('mbstring.func_overload') & 2)
		self.Error('mbstring overloading must be disabled')
	#Disable runtime magic quotes
	if(get_magic_quotes_runtime())
		@set_magic_quotes_runtime(0)
	"""
        return True

 def __getpageformat__(self,format):
	format=str(format).lower()
	if(not self.PageFormats.has_key(format)):
		self.Error('Unknown page format: '.format)
	a=self.PageFormats[format]
	return [a[0]/self.k, a[1]/self.k]

 def __UTF8toUTF16__(self,s):
	return s.encode("utf-16")


 def __getfontpatht__(self):
	"""
	if(! defined('FPDF_FONTPATH') and is_dir(dirname(__FILE__).'/font'))
		 define('FPDF_FONTPATH',dirname(__FILE__).'/font/')
	return  defined('FPDF_FONTPATH') ? FPDF_FONTPATH : ''
	"""
	return 'font.'


 def __beginpage__(self,orientation, format):
	"create a new page"
	self.page+=1
	self.pages[self.page]=''
	self.state=2
	self.x=self.lMargin
	self.y=self.tMargin
	self.FontFamily=''
	#Check page size
	if(orientation==''):
		orientation=self.defOrientation
	else:
		orientation=orientation[0].upper()
	if(format==''):
		format=self.defPageFormat
	else:
		if(isinstance(format,str)):
			format=self.__getpageformat__(format)
	if(not orientation==self.CurOrientation or not format[0]==self.CurPageFormat[0] or not format[1]==self.CurPageFormat[1]):
		#New size
		if(orientation=='P'):
			self.w=format[0]
			self.h=format[1]
		else:
			self.w=format[1]
			self.h=format[0]
		self.wPt=self.w*self.k
		self.hPt=self.h*self.k
		self.PageBreakTrigger=self.h-self.bMargin
		self.CurOrientation=orientation
		self.CurPageFormat=format
	if(not orientation==self.defOrientation or not format[0]==self.defPageFormat[0] or not format[1]==self.defPageFormat[1]):
		self.PageSizes[self.page]=array(self.wPt, self.hPt)
	

 def __endpage__(self):
	self.state=1

 def __escape__(self,s):
	#Escape special characters in strings
	s=s.replace('\\','\\\\')
	s=s.replace('(','\\(')
	s=s.replace(')','\\)')
	s=s.replace("\r",'\\r')
	return s

 def __textstring__(self,s):
	#Format a text string
	return '('+self.__escape__(s)+')'

 def __dounderline__(self,x, y, txt):
	#Underline text
	up=self.CurrentFont['up']
	ut=self.CurrentFont['ut']
	w=self.GetStringWidth(txt)+self.ws*substr_count(txt,' ')
	return '%.2F %.2F %.2F %.2F re f'%(x*self.k,(self.h-(y-up/1000*self.FontSize))*self.k,w*self.k,-ut/1000*self.FontSizePt)

 def __parsejpg__(self,file):
	#Extract info from a JPEG file
	a=GetImageSize(file)
	if(not a):
		self.Error('Missing or incorrect image file: '.file)
	if(not a[2]==2):
		self.Error('Not a JPEG file: '.file)
	if(not a.has_key('channels') or a['channels']==3):
		colspace='DeviceRGB'
	elif(a['channels']==4):
		colspace='DeviceCMYK'
	else:
		colspace='DeviceGray'
	#bpc=isset(a['bits']) ? a['bits'] : 8
        bpc=8
	if a.has_key('bits'):
		bpc=a['bits']
	#Read whole file
	f=fopen(file,'rb')
	data=''
	while(not EOF):
		data+=fread(f,8192)
	fclose(f)
	return {'w':a[0], 'h':a[1], 'cs':colspace, 'bpc':bpc, 'f':'DCTDecode', 'data':data}

 def __parsepng__(self,file):
	#Extract info from a PNG file
	f=fopen(file,'rb')
	if(not f):
		self.Error('Can\'t open image file: '+file)
	#Check signature
	if(not self.__readstream__(f,8)==chr(137)+'PNG'+chr(13)+chr(10)+chr(26)+chr(10)):
		self.Error('Not a PNG file: '.file)
	#Read header chunk
	self.__readstream__(f,4)
	if(not self.__readstream__(f,4)=='IHDR'):
		self.Error('Incorrect PNG file: '+file)
	w=self.__readint__(f)
	h=self.__readint__(f)
	bpc=ord(self.__readstream__(f,1))
	if(bpc>8):
		self.Error('16-bit depth not supported: '+file)
	ct=ord(self.__readstream__(f,1))
	if(ct==0):
		colspace='DeviceGray'
	elif(ct==2):
		colspace='DeviceRGB'
	elif(ct==3):
		colspace='Indexed'
	else:
		self.Error('Alpha channel not supported: '+file)
	if(not ord(self.__readstream__(f,1))==0):
		self.Error('Unknown compression method: '+file)
	if(not ord(self.__readstream__(f,1))==0):
		self.Error('Unknown filter method: '+file)
	if(not ord(self.__readstream__(f,1))==0):
		self.Error('Interlacing not supported: '+file)
	self.__readstream__(f,4)
	parms='/DecodeParms <</Predictor 15 /Colors '
	#parms+=(ct==2 ? 3 : 1)
	if ct==2:
		parms+=str(3)
	else:
		parms+=str(1)
	parms+=' /BitsPerComponent '+str(bpc)+' /Columns '+str(w)+'>>'
	#Scan chunks looking for palette, transparency and image data
	pal=''
	trns=''
	data=''
	n=True
	while(n):
		n=self.__readint__(f)
		type=self.__readstream__(f,4)
		if(type=='PLTE'):
			#Read palette
			pal=self.__readstream__(f,n)
			self.__readstream__(f,4)
		elif(type=='tRNS'):
			#Read transparency info
			t=self.__readstream__(f,n)
			if(ct==0):
				trns=[ord(t[1,2])]
			elif(ct==2):
				trns=[ord(t[1,1]), ord(t[3,4]), ord(t[5,6])]
			else:
				pos=t.find(chr(0))
				if(not pos<0):
					trns=[pos]
			self.__readstream__(f,4)
		elif(type=='IDAT'):
			#Read image data block
			data+=self.__readstream__(f,n)
			self.__readstream__(f,4)
		elif(type=='IEND'):
			break
		else:
			self.__readstream__(f,n+4)
	if(colspace=='Indexed' and empty(pal)):
		self.Error('Missing palette in '.file)
	fclose(f)
	return {'w':w, 'h':h, 'cs':colspace, 'bpc':bpc, 'f':'FlateDecode', 'parms':parms, 'pal':pal, 'trns':trns, 'data':data}

 def __readstream__(self,f, n):
	#Read n bytes from stream
	res=''
	while(n>0 and not EOF):
		s=fread(f,n)
		if(s==False):
			self.Error('Error while reading stream')
		n-=len(s)
		res+=s
	if(n>0):
		self.Error('Unexpected end of stream')
	return res

 def __readint__(self,f):
	# faire la methode unpack
	#Read a 4-byte integer from stream
	a=unpack('Ni',self.__readstream__(f,4))
	return a['i']

 def __parsegif__(self,file):
	#Extract info from a GIF file (via PNG conversion)
	if(not function_exists('imagepng')):
		self.Error('GD extension is required for GIF support')
	if(not function_exists('imagecreatefromgif')):
		self.Error('GD has no GIF read support')
	im=imagecreatefromgif(file)
	if(not im):
		self.Error('Missing or incorrect image file: '.file)
	imageinterlace(im,0)
	tmp=tempnam('.','gif')
	if(not tmp):
		self.Error('Unable to create a temporary file')
	if(not imagepng(im,tmp)):
		self.Error('Error while saving to temporary file')
	imagedestroy(im)
	info=self.__parsepng__(tmp)
	unlink(tmp)
	return info

 def __newobj__(self):
	#Begin a new object
	self.n=str(int(self.n)+1)
	self.offsets[self.n]=len(self.buffer)
	self.__out__(self.n+' 0 obj')

 def __putstream__(self,s):
	self.__out__('stream')
	self.__out__(s)
	self.__out__('endstream')

 def __out__(self,s):
	#Add a line to the document
	if(self.state==2):
		self.pages[self.page]+=str(s)+"\n"
	else:
		self.buffer+=str(s)+"\n"

 def __putpages__(self):
	nb=int(self.page)
        if(len(self.AliasNbPages())>0):
		#Replace number of pages
		for n in range(1,nb+1):
			n=str(n)
			if self.pages.has_key(str(n)):
				self.pages[n]=self.pages[n].replace(self.AliasNbPages(),nb)
	if(self.defOrientation=='P'):
		wPt=self.defPageFormat[0]*self.k
		hPt=self.defPageFormat[1]*self.k
	else:
		wPt=self.defPageFormat[1]*self.k
		hPt=self.defPageFormat[0]*self.k
	#filter=(self.compress) ? '/Filter /FlateDecode ' : ''
	filter=''
	if self.compress:
		filter='/Filter /FlateDecode '	
	for n in self.pages.keys():
		#Page
		self.__newobj__()
		self.__out__('<</Type /Page')
		self.__out__('/Parent 1 0 R')
		if(self.PageSizes.has_key(n)):
			self.__out__('/MediaBox [0 0 %.2F %.2F]'%(self.PageSizes[n][0],self.PageSizes[n][1]))
		self.__out__('/Resources 2 0 R')
		if(self.PageLinks.has_key(n)):
			#Links
			annots='/Annots ['
			for pl in self.PageLinks[n]:
				rect='%.2F %.2F %.2F %.2F'%(pl[0],pl[1],pl[0]+pl[2],pl[1]-pl[3])
				annots+='<</Type /Annot /Subtype /Link /Rect ['+rect+'] /Border [0 0 0] '
				if(isinstance(pl[4],str)):
					annots+='/A <</S /URI /URI '+self.__textstring__(pl[4])+'>>>>'
				else:
					l=self.links[pl[4]]
					#h=isset(self.PageSizes[l[0]]) ? self.PageSizes[l[0]][1] : hPt
					h=hPt
					if len(self.PagesSizes[l[0]])>2:
						h=self.PageSizes[l[0]][1]
					annots+='/Dest [%d 0 R /XYZ 0 %.2F None]>>'%(1+2*l[0],h-l[1]*self.k)
			self.__out__(str(annots)+']')
		self.__out__('/Contents '+str(int(self.n)+1)+' 0 R>>')
		self.__out__('endobj')
		#Page content
		#p=(self.compress) ? gzcompress(self.pages[n]) : self.pages[n]
		p=self.pages[n]
		if self.compress:
			p=compress(self.pages[n])
		self.__newobj__()
		self.__out__('<<'+filter+'/Length '+str(len(p))+'>>')
		self.__putstream__(p)
		self.__out__('endobj')
	#Pages root
	self.offsets['1']=len(self.buffer)
	self.__out__('1 0 obj')
	self.__out__('<</Type /Pages')
	kids='/Kids ['
	for i in range(0,nb):
		kids+=str(3+2*i)+' 0 R '
	self.__out__(kids+']')
	self.__out__('/Count '+str(nb))
	self.__out__('/MediaBox [0 0 %.2F %.2F]'%(wPt,hPt))
	self.__out__('>>')
	self.__out__('endobj')
	

 def __putfonts__(self):
	nf=self.n
	for diff in self.diffs:
		#Encodings
		self.__newobj__()
		self.__out__('<</Type /Encoding /BaseEncoding /WinAnsiEncoding /Differences ['+diff+']>>')
		self.__out__('endobj')
	for file in self.FontFiles: # as file=>info)
		#Font file embedding
		info = self.FontFiles[file]
		self.__newobj__()
		self.FontFiles[file]['n']=self.n
		font=''
		f=fopen(self.__getfontpatht__().file,'rb',1)
		if(not f):
			self.Error('Font file not found')
		while(not EOF):
			font+=fread(f,8192)
		fclose(f)
		compressed=(substr(file,-2)=='.z')
		if (not compressed and info.has_key('length2')):
			header=(ord(font[0])==128)
			if(header):
				#Strip first binary header
				font=substr(font,6)
			if(header and ord(font[info['length1']])==128):
				#Strip second binary header
				font=font[0:info['length1']]+font[info['length1']+6:len(font)]
		self.__out__('<</Length '.len(font))
		if(compressed):
			self.__out__('/Filter /FlateDecode')
		self.__out__('/Length1 '+info['length1'])
		if(info.has_key('length2')):
			self.__out__('/Length2 '+info['length2']+' /Length3 0')
		self.__out__('>>')
		self.__putstream__(font)
		self.__out__('endobj')
	for k in self.fonts.keys(): # as k=>font
		#Font objects
		font=self.fonts[k]
		self.fonts[k]['n']=int(self.n)+1
		type=font['type']
		name=font['name']
		if(type=='core'):
			#Standard font
			self.__newobj__()
			self.__out__('<</Type /Font')
			self.__out__('/BaseFont /'+name)
			self.__out__('/Subtype /Type1')
			if(not name=='Symbol' and not name=='ZapfDingbats'):
				self.__out__('/Encoding /WinAnsiEncoding')
			self.__out__('>>')
			self.__out__('endobj')
		elif (type=='Type1' or type=='TrueType'):
			#Additional Type1 or TrueType font
			self.__newobj__()
			self.__out__('<</Type /Font')
			self.__out__('/BaseFont /'+name)
			self.__out__('/Subtype /'+type)
			self.__out__('/FirstChar 32 /LastChar 255')
			self.__out__('/Widths '+str(self.n+1)+' 0 R')
			self.__out__('/FontDescriptor '+str(self.n+2)+' 0 R')
			if(font['enc']):
				if (font.has_key('diff')):
					self.__out__('/Encoding '+str(nf+font['diff'])+' 0 R')
				else:
					self.__out__('/Encoding /WinAnsiEncoding')
			self.__out__('>>')
			self.__out__('endobj')
			#Widths
			self.__newobj__()
			cw=font['cw']
			s='['
			for i in range(32,256):
				s+=cw[chr(i)]+' '
			self.__out__(s+']')
			self.__out__('endobj')
			#Descriptor
			self.__newobj__()
			s='<</Type /FontDescriptor /FontName /'+name
			for k in font['desc'] : #as k=>v)
				s+=' /'+k+' '+v
			file=font['file']
			if(file):
				s+=' /FontFile'
				#s+=(type=='Type1' ? '' : '2')
				if (type=='Type1'):
					s+=''
				else:
					s+='2'
				s+=' '+str(self.FontFiles[file]['n'])+' 0 R'
			self.__out__(s+'>>')
			self.__out__('endobj')
		else:
			#Allow for additional types
			mtd='_put'+type.lower()
			if(not method_exists(this,mtd)):
				self.Error('Unsupported font type: '.type)
			self.mtd(font)

 def __putimages__(self):
	#filter=(self.compress) ? '/Filter /FlateDecode ' : ''
	filter=''
	if (self.compress): 
		filter='/Filter /FlateDecode '
	#reset(self.images)
	#while(list(file,info)==each(self.images)):
	for fields in self.images:
 		file=''
		if len(fields)>1:
			file=fields[0]
		info=''
		if len(fields)>1:
			info=fields[1]
		self.__newobj__()
		self.images[file]['n']=self.n
		self.__out__('<</Type /XObject')
		self.__out__('/Subtype /Image')
		self.__out__('/Width '+info['w'])
		self.__out__('/Height '+info['h'])
		if(info['cs']=='Indexed'):
			self.__out__('/ColorSpace [/Indexed /DeviceRGB '+str(len(info['pal'])/3-1)+' '+str(self.n+1)+' 0 R]')
		else:
			self.__out__('/ColorSpace /'+info['cs'])
			if(info['cs']=='DeviceCMYK'):
				self.__out__('/Decode [1 0 1 0 1 0 1 0]')
		self.__out__('/BitsPerComponent '+info['bpc'])
		if(info.has_key('f')):
			self.__out__('/Filter /'+info['f'])
		if(info.has_key('parms')):
			self.__out__(info['parms'])
		if(info.has_key('trns') and info.has_key('trns') and len(info['trns'])>0):
			trns=''
			for i in range(0,len(info['trns'])):
				trns+=info['trns'][i]+' '+info['trns'][i]+' '
			self.__out__('/Mask ['+trns+']')
		self.__out__('/Length '+str(len(info['data']))+'>>')
		self.__putstream__(info['data'])
		unset(self.images[file]['data'])
		self.__out__('endobj')
		#Palette
		if(info['cs']=='Indexed'):
			self.__newobj__()
			#pal=(self.compress) ? gzcompress(info['pal']) : info['pal']
			pal=info['pal']
			if self.compress:
				pal=decompress(info['pal'])
			self.__out__('<<'+filter+'/Length '+str(len(pal))+'>>')
			self.__putstream__(pal)
			self.__out__('endobj')

 def __putxobjectdict__(self):
	for image in self.images:
		self.__out__('/I'+image['i']+' '+image['n']+' 0 R')

 def __putresourcedict__(self):
	self.__out__('/ProcSet [/PDF /Text /ImageB /ImageC /ImageI]')
	self.__out__('/Font <<')
	#print self.fonts
	for font in self.fonts.keys():
		#print font
		self.__out__('/F'+str(self.fonts[font]['i'])+' '+str(self.fonts[font]['n'])+' 0 R')
	self.__out__('>>')
	self.__out__('/XObject <<')
	self.__putxobjectdict__()
	self.__out__('>>')

 def __putresources__(self):
	self.__putfonts__()
	self.__putimages__()
	#Resource dictionary
	self.offsets['2']=len(self.buffer)
	self.__out__('2 0 obj')
	self.__out__('<<')
	self.__putresourcedict__()
	self.__out__('>>')
	self.__out__('endobj')

 def __putinfo__(self):
	self.__out__('/Producer '+self.__textstring__('FPDF-python '+str(FPDF_VERSION)+' - '+self.fpdfTranslator))
	if(self.title is not None):
		self.__out__('/Title '+self.__textstring__(self.title))
	if(self.subject is not None):
		self.__out__('/Subject '+self.__textstring__(self.subject))
	if(self.author is not None):
		self.__out__('/Author '.self.__textstring__(self.author))
	if(self.keywords is not None):
		self.__out__('/Keywords '.self.__textstring__(self.keywords))
	if(self.creator is not None):
		self.__out__('/Creator '.self.__textstring__(self.creator))
	self.__out__('/CreationDate '+self.__textstring__('D:'+str(datetime.now().strftime('%Y%m%d%H%M%I'))))


 def __putcatalog__(self):
	self.__out__('/Type /Catalog')
	self.__out__('/Pages 1 0 R')
	if(self.ZoomMode=='fullpage'):
		self.__out__('/OpenAction [3 0 R /Fit]')
	elif(self.ZoomMode=='fullwidth'):
		self.__out__('/OpenAction [3 0 R /FitH null]')
	elif(self.ZoomMode=='real'):
		self.__out__('/OpenAction [3 0 R /XYZ null null 1]')
	elif(not isinstance(self.ZoomMode,str)):
		self.__out__('/OpenAction [3 0 R /XYZ null  null '+str(self.ZoomMode/100)+']')
	if(self.LayoutMode=='single'):
		self.__out__('/PageLayout /SinglePage')
	elif(self.LayoutMode=='continuous'):
		self.__out__('/PageLayout /OneColumn')
	elif(self.LayoutMode=='two'):
		self.__out__('/PageLayout /TwoColumnLeft')

 def __putheader__(self):
	self.__out__('%PDF-'+self.PDFVersion)
	self.__out__('%‚„œ”')


 def __puttrailer__(self):
	self.__out__('/Size '+str(int(self.n)+1))
	self.__out__('/Root '+str(self.n)+' 0 R')
	self.__out__('/Info '+str(int(self.n)-1)+' 0 R')


 def __enddoc__(self):
	self.__putheader__()
	self.__putpages__()
	self.__putresources__()
	#Info
	self.__newobj__()
	self.__out__('<<')
	self.__putinfo__()
	self.__out__('>>')
	self.__out__('endobj')
	#Catalog
	self.__newobj__()
	self.__out__('<<')
	self.__putcatalog__()
	self.__out__('>>')
	self.__out__('endobj')
	#Cross-ref
	o=len(self.buffer)
	self.__out__('xref')
	self.__out__('0 '+str(int(self.n)+1))
	self.__out__('0000000000 65535 f ')
	for i in range(1,int(self.n)+1):
		if self.offsets.has_key(str(i)):
			self.__out__('%010d 00000 n '%(int(self.offsets[str(i)])))
	#Trailer
	self.__out__('trailer')
	self.__out__('<<')
	self.__puttrailer__()
	self.__out__('>>')
	self.__out__('startxref')
	self.__out__(o)
	self.__out__('%%EOF')
	self.state=3






comment="""


#Handle special IE contype request
if(isset(_SERVER['HTTP_USER_AGENT']) and _SERVER['HTTP_USER_AGENT']=='contype')
	header('Content-Type: application/pdf')
	exit

"""

exemples="""


Python 2.5.1 (r251:54863, Apr 18 2007, 08:51:08) [MSC v.1310 32 bit (Intel)] on
win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from pdf.fpdf import *
>>> myPdf=FPDF()
>>> print myPdf.fpdfTranslator
http://www.t-servi.com
>>> myPdf.AddPage()
>>> myPdf.SetFont('Times','',72)
>>> myPdf.Cell(40,10,'Hello!')
>>> myPdf.Output('test.pdf')
>>> ^Z

Python 2.5.1 (r251:54863, Apr 18 2007, 08:51:08) [MSC v.1310 32 bit (Intel)] on
win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from pdf.fpdf import *
>>> myPdf=FPDF()
>>> myPdf.AddPage()
>>> myPdf.SetFont('Arial','',50)
>>> myPdf.Cell(40,10,'Hello world !')
>>> myPdf.Output('test.pdf')
>>> ^Z


Python 2.5.1 (r251:54863, Apr 18 2007, 08:51:08) [MSC v.1310 32 bit (Intel)] on
win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from pdf.fpdf import *
>>> myPdf=FPDF()
>>> myPdf.AddPage()
>>> myPdf.SetFont('Arial','',50)
>>> myPdf.Cell(40,10,'Hello world !')
>>> myPdf.Output('test.pdf')
>>> ^Z


Python 2.5.1 (r251:54863, Apr 18 2007, 08:51:08) [MSC v.1310 32 bit (Intel)] on
win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from pdf.fpdf import *
>>> myPdf=FPDF()
>>> myPdf.AddPage()
>>> myPdf.SetLineWidth(10)
>>> myPdf.SetDrawColor(255,0,0)
>>> myPdf.SetFillColor(150,150,150)
>>> myPdf.Rect(10,10,150,150,'F')
>>> myPdf.Output('test.pdf')
>>> ^Z


Python 2.5.1 (r251:54863, Apr 18 2007, 08:51:08) [MSC v.1310 32 bit (Intel)] on
win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from pdf.fpdf import *
>>> myPdf=FPDF()
>>> myPdf.AddPage()
>>> myPdf.SetLineWidth(10)
>>> myPdf.SetDrawColor(255,0,0)
>>> myPdf.SetFillColor(150,150,150)
>>> myPdf.Rect(10,10,150,150,'DF')
>>> myPdf.Output('test.pdf')
>>>
"""


