# coding=UTF-8
# exemple repris depuis http://effbot.org/librarybooks/simplehttpserver.html
# créer un serveur http qui permet de gérer les requetes standards HEAD et GET
# en fait c'est un simple serveur de fichier html ou autre basé sur le répertoire courant
# le serveur n'interprète pas le python ou un autre language de script
# tuer le processus pour arrêter le serveur
# ce serveur ne permet pas d'utiliser les lettres de lecteurs et les chemins relatifs comme ..
# il faut cependant faire attention a son utilisation car il fait aucun contrôle de sécurité


import SimpleHTTPServer
import SocketServer

myPort=8000 						# port standard pour les tests
myHandler= SimpleHTTPServer.SimpleHTTPRequestHandler	# initialisation du gestionnaire
myHttpd=SocketServer.TCPServer(("",myPort),myHandler)   # instanciation du serveur
print "server at port "+str(myPort)			# un petit message
myHttpd.serve_forever()					# démarrage du serveur
	