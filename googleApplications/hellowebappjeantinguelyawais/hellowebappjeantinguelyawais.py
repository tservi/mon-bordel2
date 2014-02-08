# -*- coding: iso-8859-15 -*-

import wsgiref.handlers

from google.appengine.ext import webapp

class MainPage(webapp.RequestHandler):
  def get(self):  
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write('Hello, webapp wonderfull World!\n')
    self.response.out.write('What a funny thing!\n')
    self.response.out.write(str(self.request)) # dans ce cas, c'est la requete envoyée par le client
  

def main():
  application = webapp.WSGIApplication(
                                       [('/', MainPage)],
                                       debug=True) # permet de visionner le debug dans la console
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
  main()