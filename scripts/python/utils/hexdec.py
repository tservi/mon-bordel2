# coding=UTF-8

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

test="""
myDec='testjk'
myHex=dec2hex(myDec)
print myHex
print hex2dec(myHex[0:-1])
"""