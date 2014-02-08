#####################################################################
#  python code for the integration of saferpay in a zope webserver  #
#  this file must be named saferpay.py and then comes in Extensions #
#    after you must define 3 external method for the 3 functions    #
#        eport your questions to jeantinguelyawais @ gmail.com      #
#                      year created : 2006                          #
#####################################################################

import os

path="/opt/zope/saferpay/out"

def saferpay_conf(username,password):
	mes="error"
	cmd=path+"/saferpay  -conf -p "+path+" -r https://www.saferpay.com/user/setup.asp -u "+username+" -w "+password
	mes=os.popen(cmd+" 2>&1").read()
	return mes



def saferpay_payinit(total,accountid,backlink,faillink,successlink):
	url="error"
	a=" -a "
	amount=a+"AMOUNT "+total
	currency=a+"CURRENCY CHF "
	description=a+"DESCRIPTION yourgeneraldescription"
	allowcollect=a+"ALLOWCOLLECT no"
	accountid=a+"ACCOUNTID "+accountid
	backlink=a+"BACKLINK "+backlink
	faillink=a+"FAILLINK "+faillink
	successlink=a+"SUCCESSLINK "+successlink
	delivery=a+"DELIVERY no"
	cmd=path+"/saferpay -payinit -p "+path+amount+currency+description+allowcollect+accountid+backlink+faillink+successlink+delivery
	url=os.popen(cmd).read()
	return url



def saferpay_payconfirm(data,signature):
	mes1= mes2 ="error"
	if not os.path.exists(path+'/index.txt'):
		f=file(path+'/index.txt','w+')
		f.write(str(1))
		f.close()
	f=file(path+"/index.txt","r+")
	i=int(f.readline())
	i=i+1
	f.close()
	f=file(path+"/index.txt","w+")
	f.write(str(i))
	f.close()
	#d=urllib.quote(data)
	cmd=path+'/saferpay -payconfirm -p '+path+' -d \''+data+'\' -s '+signature+' -f '+path+'/'+str(i)+'.xml'
	mes1=os.popen(cmd+" 2>&1 3>&1").read()
	cmd=path+'/saferpay -capt -p '+path+' -f '+path+'/'+str(i)+'.xml'
	mes2=os.popen(cmd+" 2>&1 3>&1").read()
	return [mes1 , mes2]
	

