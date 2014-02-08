# coding=UTF-8
#
# todo :
# -------
# intÈgration des commentaires avec le %
# xref dissociÈes, par exemple de 0 ‡ 5 puis de 10 ‡ 25
#
# renseignements :
# ----------------
# savoir si on peut mettre un dictionnaire dans un array

from inspect import *

EndOfLine=['\r\n','\r','\n']  				     # \r = 13 , \n  = 10
WhiteSpaces=['\x00','\x09','\x0a','\x0c','\x0d','\x20']
delimiters=['(',')','<','>','[',']','{','}','/','%']
comments={'begin':['%'], 'end':EndOfLine}
basicTypes=['boolean','number','strings','name','array','dictionnary','stream','null']
basicBooleanValues=['false','true']
basicStringTypes=[{'name':'litteral','begin':delimiters[0],'end':delimiters[1]},{'name':'hexadecimal','begin':delimiters[2],'end':delimiters[3]}]
nameDelimiter=delimiters[8]

def hex2dec(val):
	ret=''
	top=int((len(val)+1)/2)
	for x in range(0,top):
		change=''
		if len(val)>2*x:
			change=val[2*x]
		else:
			change='0'
		if len(val)>2*x+1:
			change+=val[2*x+1]
		else:
			change+='0'
		ret+=str(chr(int('0x'+change,16)))
	return ret

def dec2hex(val):
	ret=''
	for x in val:
		ret+="%X"%(ord(x))
	return ret

class contentBoolean(object):

	def __init__(self,val=basicBooleanValues[0]):
		if val in basicBooleanValues:
			self.val=val
		else:
			self.val=basicBooleanValues[0]

	def out(self):
		return self.val

class contentNumber(object):

	def __init__(self, val=0):
		self.val=val

	def out(self):
		return self.val	
	
class contentLiteralString(object):

	def __init__(self, val=''):
		replacements=[['\n','\\n'],['\r','\\r'],['\t','\\t'],['\b','\\b'],['\f','\\f']]
		for x in replacements:
			val=val.replace(x[0],x[1])
		self.val=val

	def out(self):
		return '('+self.val+')'

class contentHexString(object):

	def __init__(self,val=''):
		self.val=val

	def out(self):
		return '<'+self.val+'>'

class contentName(object):

	def __init__(self,val=''):
		self.val=val.replace(' ','_')

	def out(self):
		return '/'+self.val

class contentArray(object):

	def __init__(self, val=[]):
		self.val=[]
		for x in val:
			if isinstance(x,list):
				self.val.append(contentArray(x))
			else:
				self.val.append(x)

	def out(self):
		ret='[ '
		for x in self.val:
			if dict(getmembers(x)).has_key('out'):
				ret+=x.out()+' '
			else:
				ret+=str(x)+' '
		ret=ret[0:-1]
		ret+=']'
		return ret

class contentDictionnary(object):

	def __init__(self, val={}):
		self.val={}
		for x in val.keys():
			# si changements ici, aussi adapter addKeyVal
			if isinstance(val[x],list):
				self.val[x]=contentArray(val[x])
			elif isinstance(val[x],dict):
				self.val[x]=contentDictionnary(val[x])
			else:
				self.val[x]=val[x]

	def addKeyVal(self,key,val):
		if isinstance(val,list):
			self.val[key]=contentArray(val)
		elif isinstance(val,dict):
			self.val[key]=contentDictionnary(val)
		else:
			self.val[key]=str(val)

	def out(self):
		ret='<< '
		for x in self.val.keys():
			if dict(getmembers(self.val[x])).has_key('out'):
				ret+='/'+str(x)+' '+self.val[x].out()+' '+EndOfLine[0]
			else:
				ret+='/'+str(x)+' '+str(self.val[x])+' '+EndOfLine[0]
		ret+='>>'
		return ret

class contentNull(object):

	def __init__(self):
		self.val='null'

	def out(self):
		return self.val

class contentStream(object):

	def __init__(self,val={'dictionnary': {},'stream': contentNull()}):
		# le champs Length est requis et est calculÈ
                # champs possibles dans la version 1.7: 
		# Filter, DecodeParms, F, FFilter, FDecodeParms, DL
		self.val={'dictionnary':contentDictionnary(),'stream':''}
		if val.has_key('stream'):
			self.val['stream']=val['stream']
		if dict(getmembers(self.val['stream'])).has_key('out'):
			self.val['dictionnary'].addKeyVal('Length',len(str(self.val['stream'].out())))
		else:
			self.val['dictionnary'].addKeyVal('Length',len(str(self.val['stream'])))
		if val.has_key('dictionnary'):
			if isinstance(val['dictionnary'],dict):
				for key in val['dictionnary'].keys():
					self.val['dictionnary'].addKeyVal(key,val['dictionnary'][key])	
	
	def out(self):
		ret=''
		ret+=self.val['dictionnary'].out()
		ret+=EndOfLine[0]
		ret+='stream'+EndOfLine[0]
		if dict(getmembers(self.val['stream'])).has_key('out'):
			ret+=self.val['stream'].out()
		else:
			ret+=str(self.val['stream'])
		ret+=EndOfLine[0]
		ret+='endstream'
		return ret

class structureCatalog(object):

	def __init__(self):
		pass

	def out(self):
		pass
		
class PDFObject(object):

	def __init__(self, number=1, generation=0, content=contentNull(), free='n',next=0,offset=None):
		self.number=number
		self.generation=generation
		self.free=free
		self.offset=offset
		self.next=next
		self.content=content

        def contentOut(self):
		ret=''       
		if self.free=='n': 
			ret+=str(self.content.out()) 
		return ret

	def changeContent(self , object = contentNull() ):
		self.content=object

	def bodyOut(self):
		ret=''
		ret+=str(self.number)+' '+str(self.generation)+' obj '+EndOfLine[0]
		ret+=self.contentOut()
		ret+=EndOfLine[0]
		ret+='endobj'+EndOfLine[0]
		return ret

	def xrefOut(self):
		ret=''
		#if self.offset is not None:
		if self.free=='n':
			ret+='%010d %05d n '%(int(self.offset),int(self.generation))
		else:
			ret+='%010d %05d f '%(int(self.next),int(self.generation))
		ret+=EndOfLine[0]
		return ret
		
class PDFVersion(object):
	
	def __init__(self,objects=[]):
		self.objects=objects
		if len(self.objects)==0:
			self.addObject0()

	def changeContent(self , obj=1, object = contentNull() ):
		if len(self.objects)>obj:
			self.objects[obj].changeContent(object)

	def addObject0(self):
		self.objects.append(PDFObject(0,65535, contentNull(), 'f',0))	


	def addObject(self, number=1, generation=0,content=contentNull()):
		object=PDFObject(number, generation, content)
		self.objects.append(object)

	def bodyOut(self,offset):
		ret=''
		for x in self.objects:
			if not x.free=='f':
				x.offset=offset
				add=x.bodyOut()
				ret+=add
				offset+=len(add)
		return ret
				
	def xrefOut(self):
		ret=''
		ret+='xref'+EndOfLine[0]
		min=65535
		for x in self.objects:
			if x.number<min:
				min=x.number
		ret+=str(min)+' '+str(len(self.objects))+EndOfLine[0]
		for x in self.objects:
			ret+=x.xrefOut()
		return ret

	def trailerOut(self,startxref=0):
		ret=''
		ret+='trailer'+EndOfLine[0]
		root=' 1 0 R '
		max=0
		min=65535
		for x in self.objects:
			if x.number>max:
				max=int(x.number)+1
			if x.number<min and not x.free=='f':
				min=x.number
				root=' '+str(min)+' '+str(x.generation)+' R '
		ret+='<< /Size '+str(max)+' '+EndOfLine[0]+'/Root '+str(root)+' >>'+EndOfLine[0]
		ret+='startxref'+EndOfLine[0]
		ret+=str(startxref)+EndOfLine[0]
		ret+='%%EOF'
		return ret
	
	def out(self,offset=0):
		ret=''
		ret+=self.bodyOut(offset)
		startxref=len(ret)+offset+6
		ret+=self.xrefOut()
		ret+=self.trailerOut(startxref)
		return ret	
		
class PDF(object):
	
	def __init__(self,version='1.7'):
		self.PDFVersion=version
		original=PDFVersion()
		self.versions=[original]

        def changeContent(self, version=0, obj=0, content=contentNull()):
		if version<len(self.versions):
			self.versions[version].changeContent(obj, content)

	def addObject(self, version=0, number=1, generation=0,content=contentNull()):
		if len(self.versions)>version:
			self.versions[version].addObject(number, generation, content)

	def outHeader(self):	
		return '%PDF-'+self.PDFVersion+'\n%‚„œ”\n\n'

	def out(self,fileName):
		f=open(fileName,'w+')
		buffer=''
		buffer+=self.outHeader()
		for version in self.versions:
			offset=len(buffer)
			buffer+=version.out(offset)
		f.write(buffer)
		f.close()


print dec2hex('testk')
print hex2dec('901FA3')
myPdf=PDF()
content=contentBoolean()
#myPdf.addObject(0,1,0,content)
myPdf.addObject()
print content
print myPdf.versions[0].objects[1].content
myPdf.changeContent(0,1,content)
print myPdf.versions[0].objects[1].content
content=contentNumber(-100.00)
myPdf.changeContent(0,1,content)
print content
print myPdf.versions[0].objects[1].content
content=contentLiteralString('test\ntest	test')
myPdf.changeContent(0,1,content)
print content
print myPdf.versions[0].objects[1].content
content=contentName('This.is.a.test')
myPdf.changeContent(0,1,content)
print content
print myPdf.versions[0].objects[1].content
content=contentArray(['this','is','a',['very',['very',['very']],'special'],'test'])
myPdf.changeContent(0,1,content)
print content
print myPdf.versions[0].objects[1].content
contentDictionnary
content=contentDictionnary({'1':'un','2':'deux'})
content.addKeyVal('3','trois')
myPdf.changeContent(0,1,content)
print content
print myPdf.versions[0].objects[1].content
content=contentStream({'dictionnary':{'1':'un','2':'deux'},'stream':contentArray(['this','is','a',['very',['very',['very']],'special'],'test'])})
myPdf.changeContent(0,1,content)
print content
print myPdf.versions[0].objects[1].content
# exemple hello world!
content=contentDictionnary({'Type':contentName('Catalog'),'Outlines':'2 0 R','Pages':'3 0 R'})
myPdf.changeContent(0,1,content)
content=contentDictionnary({'Type':contentName('Outlines'),'Count':'0'})
myPdf.addObject(0,2,0,content)
content=contentDictionnary({'Type':contentName('Pages'),'Kids':contentArray(['4 0 R']),'Count':'1'})
myPdf.addObject(0,3,0,content)
content=contentDictionnary({'Type':contentName('Page'),'Parent':'3 0 R','Mediabox':[0,0,612,792],'Contents':'5 0 R','Ressources':{'ProcSet':'6 0 R','Font':{'F1':'7 0 R'}}})
myPdf.addObject(0,4,0,content)
content=contentStream({'dictionnary':'','stream':'BT\n/F1 24 Tf\n1.0 0 0 0 k\n100 100 Td\n( Hello world ) Tj\nET'})
myPdf.addObject(0,5,0,content)
content=contentArray([contentName('PDF'),contentName('Text')])
myPdf.addObject(0,6,0,content)
content=contentDictionnary({'Type':contentName('Font'),'Subtype':contentName('Type1'),'Name':contentName('F1'),'BaseFont':contentName('Helvetica'),'Encoding':contentName('MacRomanEncoding')})
myPdf.addObject(0,7,0,content)
myPdf.out('test.pdf')
