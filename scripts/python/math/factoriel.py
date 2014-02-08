# coding=UTF-8

def factoriel(n=1):
	if n==0:
		return 1
	elif n==1:
		return 1
	else:
		return n*factoriel(n-1)

set=range(0,20)
for x in set:
	print x, factoriel(x)

