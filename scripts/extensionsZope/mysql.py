# extension zope pour utiliser une base sql dans zope

import tempfile, os, types, string
import _mysql

def table(r):
	t=[]
	if int(r.num_rows())>0:
	   for i in range(0,int(r.num_rows())):
		l=r.fetch_row()
		for x in l:
		      t.append(list(x))
        return t
		
def simple_query(query):
        ret=''
	db=_mysql.connect("127.0.0.1","user","pass","db")
	my_query="select "
	i=0
	for x in my_fields:
		my_query+=x
		if i<len(my_fields)-1:
			my_query+=", "
		i+=1
	my_query+=" from restaurants where "
	my_query+="  ( "
	# tout ce qui est au dessus est obligatoire
	j=0
	for v in query:
	  if len(query)>1:
	    if j==0:
		  my_query+=' ( '
	    else:
		  my_query+=' ) OR ( '
	  l=0
	  for w in v:
	    if len(v)>1:
		    if l==0:
			    my_query+=' ( '
		    else:
			    my_query+=' ) AND ( '
	    k=0	    
	    for x in my_fields_query:
		my_query+=x+" like '%"+w+"%'"
		if k<len(my_fields_query)-1:
			my_query+=" or "
			k+=1
		l+=1	
	    #my_query+=" )"
	  if len(v)>1:
		  my_query+=' )'
	  j+=1
	if len(query)>1:
		my_query+=' )'
	my_query+=' ) order by restaurant_wahl DESC, restaurant_name'
	#tout ce qui est en dessous est obligatoire   
	db.query(my_query)
	r1=db.store_result()
	my_t=table(r1)
	db.close()
	return my_t
	#return my_query
		
def select(query='',geo='',rub=''):
	"""
	    Manipulate the query to return the resultset from the database x1 'x2' ::OR:: x3+x4 x5
	    [[ x1 and x2] or [x3 and x4 and x5]]
	"""
	query=' '+query
	query=query.replace(',',' ')
	query=query.replace('  ',' ')
	t1=query.split('::OR::')
	t2=[]
	t4=[]
	t=''
	for x in t1:
		t+=x+' :: '
		#t3.append(x)
		t3=[]
		search=x
		if search.find('\'')>0:
			t=list(search)
			prend=True
			n_search=''
			a_search=''
			for x in t:
				if x=="'":
					if prend:
						prend=False
					else:
						prend=True
			        if prend and x!="'":
				        n_search+=x
				else:
					a_search+=x
			search=n_search
			for v in a_search.split('\''):
				if len(v)>0:
				    t3.append(v)
		if search.find('+')>0:
			t=list(search)
			prend=True
			n_search=''
			a_search=''
			for x in t:
				if x=="+":
					if prend:
						prend=False
					else:
						prend=True
			        if prend and x!="+":
				        n_search+=x
				else:
					a_search+=x
			search=n_search
			for v in a_search.split('+'):
				for w in v.split(' '):
				   if len(w)>0:
				      t3.append(w)
		for z in search.split(' '):
			if len(z)>0:
				t3.append(z)
		t2.append(t3)
	return simple_query(t2)
			

def profi(name, rub, kt, reg, ort):
	db=_mysql.connect("127.0.0.1","user","pass","db")
	my_query="select "
	i=0
	for x in my_fields:
		my_query+=x
		if i<len(my_fields)-1:
			my_query+=", "
		i+=1
	my_query+=" from restaurants where "
	for_and=0
	if len(name)>0:
		my_query+=" restaurant_name like '%"+(name.replace(',',' ')).replace(' ','%')+"%' "
		for_and+=1
	if len(ort)>0:
                if for_and>0:
                        my_query+=" and "
		my_query+=" restaurant_ort like '%"+(ort.replace(',',' ')).replace(' ','%')+"%' "
		for_and+=1
	if len(rub)>2:
		if for_and>0:
			my_query+=" and "
		my_query+=" restaurant_rubrik  like '%"+str(rub[1:-1]).replace("'","%")+"%' "
		for_and+=1
	if len(kt)>1:
		if for_and>0:
			my_query+=" and "
		my_query+=" restaurant_kanton='"+kt+"' "
		for_and+=1
	if len(reg)>2:
		if for_and>0:
			my_query+=" and "
		my_query+=" restaurant_region='"+reg+"' "
		for_and+=1
	my_query+=" order by restaurant_wahl DESC, restaurant_name "
	db.query(my_query)
	r1=db.store_result()
	my_t=table(r1)
	db.close()
	return my_t	
	#return my_query

def get_gemeinde(self):
  """
      Import the data from a file at the root of the instance
      the file must be a csv called g_nummer.csv with header : gemeinde_nummer, region, region_nummer 
  """
  ff=open('g_nummer.csv','r+')
  l0=ff.readlines()
  ff.close()
  l1=[]
  for x in l0:
    z=x.split('\r\n')
    l1.append(z[0])
  l2=[]
  for x in l1:
    z=x.split(';')
    l2.append([int(z[0]),z[1],z[2]])
  return l2
  
def get_plz(self):
  """
      Import the data from a file at the root of the instance 
      the file must be a csv called plz.csv with header : plz, name, mane_02, kt, gemeinde_nummer
  """
  ff=open('plz.csv','r+')
  l0=ff.readlines()
  ff.close()
  l1=[]
  for x in l0:
     z=x.split('\r\n')
     l1.append(z[0])
  l2=[]
  for x in l1[1:len(l1)]:
     z=x.split(';')
     l2.append(z)
  l3=[]
  for x in l2:
     l3.append([x[0],x[1],x[2],x[3],int(x[4])])   
  return l3
  		  
def prepare_restaurant(self):
 """
       Prepare the restaurant from a txt file to be inserted in the DB 
       The structure is a csv file which contains
       rubrik, name, vorname, postfach, strasse, plz ort, kanton, telefon, mobile, fax, homepage, email
 """
 f_name=self.REQUEST.form.get('my_file').filename
 ret=[]
 folder=tempfile.mktemp()
 os.mkdir(folder)
 datei=open(folder+'/'+f_name,'w+')
 datei.write(self.REQUEST.form.get('my_file').read())
 datei.close()
 datei=open(folder+'/'+f_name,'r+')
 ret=datei.readlines()
 datei.close()
 os.remove(folder+'/'+f_name)
 os.rmdir(folder)
 my_ret=[]
 for x in ret:
     my_ret.append(str(x))
 #if f_name:
 #  format=str(f_name).split('.')[-1].upper()
 #  if (format == 'JPG' or format=='JPEG'):
 #      ret = add_image(self.this(),f_name,self.REQUEST.form.get('my_file'),search_id(self.objectValues('Image')))
 #  elif format=='ZIP':
 #      val=''
 #      zip_folder=tempfile.mktemp()
 #      os.mkdir(zip_folder)
 #      zip_datei=open(zip_folder+'/'+f_name,'w+')
 #      zip_datei.write(self.REQUEST.form.get('my_file').read())
 #      zip_datei.close()
 #      zip_datei=open(zip_folder+'/'+f_name,'r+')
 #      zf = ZipFile(zip_datei)
 #      for extracted_file in zf.namelist():
 #         format=str(extracted_file).split('.')[-1].upper()
 #	  if (format == 'JPG' or format=='JPEG'):
 #	    extracted=open(zip_folder+'/'+extracted_file,'w+')
 #	    extracted.write(zf.read(extracted_file))
 #	    extracted.close()
 #	    extracted=open(zip_folder+'/'+extracted_file,'r+')
 #	    val=val+add_image(self.this(),extracted_file,extracted,search_id(self.objectValues('Image')))
 #	    extracted.close()
 #	    os.remove(zip_folder+'/'+extracted_file)
 #      zip_datei.close()
 #      os.remove(zip_folder+'/'+f_name)
 #      os.rmdir(zip_folder)
 #      ret="<br>Datei Hochgeladet und entpacket!"
 #  else:
 #      ret= "Nur jpg oder jper oder zip Datei erledigt!"
 #else:
 return my_ret


def zquery(my_server='127.0.0.1', my_user='user', my_pass='pass', my_db='db', my_query='select * from users'):
   """
        send a query to mysql
   """
   zdb=_mysql.connect(my_server,my_user,my_pass,my_db)
   zdb.query(my_query)
   try:
     ret= table(zdb.store_result())
   except:
     ret=''
   zdb.close()
   return ret



