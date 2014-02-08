# coding=UTF-8

import anydbm

class memoire(object):

	"""
	Permettre la création d'une mémoire associative
	"""


	def __init__(self,chemin=None):
		if chemin is None:
			self.chemin="memoire.data"
		else:
			self.chemin=chemin
		db=anydbm.open(self.chemin,'c')
		db.close()

	def importer(self,dict):
		db=anydbm.open(self.chemin,'c')
		for k in dict.keys():
			db[k]=dict[k]
		db.close()

	def exporter(self):
		ret={}
		db=anydbm.open(self.chemin,'c')
		for k in db.keys():
			ret[k]=db[k]
		db.close()
		return ret

	def inserer(self,cle,contexte,valeur):
		db=anydbm.open(self.chemin,'c')
		db[cle+'.'+contexte]=valeur
		db.close()

	def chercher(self,cle,contexte):
		ret=None
		db=anydbm.open(self.chemin,'c')
		if db.has_key(cle+'.'+contexte):
			ret=db[cle+'.'+contexte]
		db.close()
		return ret

test="""
myMem=memoire()
myMem.inserer('test','test1','bla')
myMem.inserer('test','test2','blou')
myMem.inserer('test','test3','bli')
myMem.inserer('test','test4','blu')
print myMem.chercher('test','test')
print myMem.exporter()
"""