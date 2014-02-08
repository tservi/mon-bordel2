# coding=UTF-8
# exemple repris depuis http://effbot.org/librarybooks/simplehttpserver.html
# création d'un proxy minimal en pyton
# la requête http est envoyée à un proxy
# ce proxy utiliser urllib pour récupérer les données de la cible

import SocketServer
import SimpleHTTPServer
import urllib

myPort=1234							# choisir un port

class Proxy(SimpleHTTPServer.SimpleHTTPRequestHandler):		# création de la classe Proxy qui hérite de SimpleHTTPRequestHandler
 def do_GET(self):						# surcharge de la méthode do_GET
  self.copyfile(urllib.urlopen(self.path), self.wfile)		# copie le tampon provenant de l'url cible et le retourne 

myHttpd=SocketServer.ForkingTCPServer(('',myPort), Proxy)	# instanciation du serveur 
print "server at port "+str(myPort)				# un petit message
myHttpd.serve_forever()						# le serveur est démarré



