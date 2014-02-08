# coding=UTF-8
# exemple repris depuis http://effbot.org/librarybooks/simplehttpserver.html
# cr�ation d'un proxy minimal en pyton
# la requ�te http est envoy�e � un proxy
# ce proxy utiliser urllib pour r�cup�rer les donn�es de la cible

import SocketServer
import SimpleHTTPServer
import urllib

myPort=1234							# choisir un port

class Proxy(SimpleHTTPServer.SimpleHTTPRequestHandler):		# cr�ation de la classe Proxy qui h�rite de SimpleHTTPRequestHandler
 def do_GET(self):						# surcharge de la m�thode do_GET
  self.copyfile(urllib.urlopen(self.path), self.wfile)		# copie le tampon provenant de l'url cible et le retourne 

myHttpd=SocketServer.ForkingTCPServer(('',myPort), Proxy)	# instanciation du serveur 
print "server at port "+str(myPort)				# un petit message
myHttpd.serve_forever()						# le serveur est d�marr�



