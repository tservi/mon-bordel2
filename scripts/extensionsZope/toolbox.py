#####################################################################
#                      year created : 2006                          #
#                  gestion d'une boite a images                     #
#####################################################################


import tempfile, os, types, string
from zipfile import *

liste_id=[]
liste_val=['_128.jpg','_200.jpg','_320.jpg','_480.jpg','_768.jpg','_1024.jpg']
liste_digit=['0','1','2','3','4','5','6','7','8','9']

def loeschen(self):
  """
        Delete a special image set from the toolbox
  """
  loeschen=self.REQUEST['loeschen']
  tit=''
  i=0
  j=0
  index=[]
  cursor=[]
  for x in self.objectValues('Image'):
    if str(x.id())[0:6] not in index:
       index.append(str(x.id())[0:6])  
       cursor.append([str(x.id())[0:6],str(x.title),[str(x.id())]])
       if str(x.id())[0:6]==loeschen:
            tit=str(x.title)
            j=i
       i=i+1
    else:
       cursor[-1][2].append(str(x.id()))
  #for val in cursor[j][2]:
      #self._delOb(self, id=str(val))
      #delet=delet+str(val)+' '
  self.manage_delObjects(ids=cursor[j][2])
  return tit+' gel&ouml;scht !'


def search_id(self,obj):
 """
       Create the new id
 """
 ##### create the new id ###########
 #for x in self.objectValues('Image'):
 for x in obj:
    liste_id.append(str(x.id())[0:6])
 for digit0 in liste_digit:
   for digit1 in liste_digit:
     for digit2 in liste_digit:
       for digit3 in liste_digit:
         for digit4 in liste_digit:
           for digit5 in liste_digit:
             searched_dict=0
             searched=str(digit0)+str(digit1)+str(digit2)+str(digit3)+str(digit4)+str(digit5)
             if(self.toolbox.hasProperty('eigene_formate')):
                  self_val=self.toolbox.getProperty('eigene_formate').split(',')
                  for x in self_val:
                    liste_val.append('_'+x+'.jpeg')
             for extension in liste_val:
               searched_extension=str(searched)
               if searched_extension in liste_id:
                 searched_dict=searched_dict+1
             if searched_dict==0:
               return searched
 return ''
        
	       
def add_image(self, f_name,file,new_id):
  """
       Add new image set in the toolbox
  """
  folder=tempfile.mktemp()
  os.mkdir(folder)
  datei=open(folder+'/'+f_name,'w+')
  datei.write(file.read())
  datei.close()
  val='' 
  liste_ext=liste_val
  if(self.toolbox.hasProperty('eigene_formate')):
    self_val=self.toolbox.getProperty('eigene_formate').split(',')
    liste_ext=[]
    for x in self_val:
      liste_ext.append('_'+x+'.jpeg')
  for extension in liste_ext:
    #cmd='/usr/bin/convert '+folder+'/'+f_name+' -resize '+extension[1:-4]+'x'+extension[1:-4]+' '+folder+'/'+new_id+extension
    cmd='/usr/bin/convert '+folder+'/'+f_name+' -resize '+extension[1:-4]+' '+folder+'/'+new_id+extension
    order=os.popen(cmd).read()
    kurz_name='_'+str(f_name.split('.')[0])
    kurz_name=kurz_name.replace(' ','_')
    val=val+self.manage_addImage(id=new_id+kurz_name+extension,file=open(folder+'/'+new_id+extension),title=f_name, precondition='', content_type='',REQUEST=None)+' ' 
    os.remove(folder+'/'+new_id+extension)
  os.remove(folder+'/'+f_name)
  os.rmdir(folder)
  txt="Datei Hochgeladen!<br>"
  #my_root=self.toolbox
  #txt+=my_root.id+"<br>"
  #if(my_root.hasProperty('eigene_formate')):
  #  txt+=my_root.getProperty('eigene_formate')+"<br>"
  return txt

  		  
def add(self):
 """
       Add new image(s) in the toolbox 
 """
 f_name=self.REQUEST.form.get('my_file').filename
 if len(f_name.split('\\'))>1:
	f_name=f_name.split('\\')[-1]
 if f_name:
   format=str(f_name).split('.')[-1].upper()
   if (format == 'JPG' or format=='JPEG' or format =='GIF' or format=='PNG'):
       ret = add_image(self.this(),f_name,self.REQUEST.form.get('my_file'),search_id(self,self.this().objectValues('Image')))
   elif format=='ZIP':
       val=''
       zip_folder=tempfile.mktemp()
       os.mkdir(zip_folder)
       zip_datei=open(zip_folder+'/'+f_name,'w+')
       zip_datei.write(self.REQUEST.form.get('my_file').read())
       zip_datei.close()
       zip_datei=open(zip_folder+'/'+f_name,'r+')
       zf = ZipFile(zip_datei)
       for extracted_file in zf.namelist():
          format=str(extracted_file).split('.')[-1].upper()
	  if (format == 'JPG' or format=='JPEG' or format =='GIF' or format=='PNG'):
	    extracted=open(zip_folder+'/'+extracted_file,'w+')
	    extracted.write(zf.read(extracted_file))
	    extracted.close()
	    extracted=open(zip_folder+'/'+extracted_file,'r+')
	    val=val+add_image(self.this(),extracted_file,extracted,search_id(self,self.this().objectValues('Image')))
	    extracted.close()
	    os.remove(zip_folder+'/'+extracted_file)
       zip_datei.close()
       os.remove(zip_folder+'/'+f_name)
       os.rmdir(zip_folder)
       ret="<br>Datei Hochgeladet und entpacket!"
   else:
       ret= "Nur jpg, jpeg, gif, png, oder zip Datei erledigt!"
 else:
  ret= "Nichts war hochgeladet! Ihr Firewall, Proxy oder Sicherheitseinstellungen einrichten!"
 return ret
 
def copy(self):
 """
     copy Images in a new destination
 """
 ret=' '
 if self.REQUEST.SESSION.has_key('my_path'):
	 zpath=self.REQUEST.SESSION['my_path'].replace('toolbox_root','').strip('/')
	 #ret=zpath
	 if self.REQUEST.SESSION.has_key('copy_bild'):
		 cp_bild=self.REQUEST.SESSION['copy_bild'].split('/')[-1].strip('/')
		 cp_path=str('/').join(self.REQUEST.SESSION['copy_bild'].split('/')[0:-1])
		 #ret+=' '+cp_path+' '+cp_bild
		 if cp_path!=zpath:
		 	n_id=search_id(self,self.restrictedTraverse(zpath).objectValues('Image'))
		 	#ret+=' '+n_id
			for x in liste_val:
				try:
					for obj in self.restrictedTraverse(cp_path).objectValues('Image'):
					   if str(obj.getId())[0:6]==cp_bild:
						my_clip=self.restrictedTraverse(cp_path).manage_copyObjects([obj.getId()])
						copied=self.restrictedTraverse(zpath).manage_pasteObjects(my_clip)
						#ret+=' new id : '+str(copied[0]['new_id'])
						#if str(copied[0]['new_id']).split('_')[0]!=n_id:
						#	self.restrictedTraverse(zpath).manage_renameObjects([str(copied[0]['new_id'])],[str(n_id+x)])
							#ret +=' False '
						#ret+='<br>\n'
				except:
					ret+=''
 else:
	 ret=' '
 return ' '
