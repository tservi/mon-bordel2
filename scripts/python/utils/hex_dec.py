# coding=UTF-8
# chaque caratère décimal est stocqué dans une chaine hexadécimale formés de hexF "digits"

hexF='2'

def hex2dec(s):
	ret=None
	if isinstance(s,str):
		val=''
		index=0
		maxi=int(hexF)
		ret=''
		for x in s:
			val+=x
 			if index==maxi-1:
				ret+=str(chr(int('0x'+val,16)))
				index=0
				val=''
			else:
				index+=1
	return ret


def dec2hex(s):
	val=None
	if isinstance(s,str):
		val=''
		for x in s:
		 val+=eval("'%0"+hexF+"X'%(ord(x))")
	return val


test="""
s=''
for x in range(0,256):
 s+=dec2hex(chr(x))
print s
print hex2dec(s)
"""
