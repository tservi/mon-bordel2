import cgi
import wsgiref.handlers
import os


from google.appengine.api import users
from google.appengine.ext import webapp

class MainPage(webapp.RequestHandler):
  def get(self):
    body=os.getcwd()
    out="""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
<title>Main page</title>
</head>
<body>
<h1>Hello world!</h1>
<br/>
%s
</body>
</html>
"""%(body)
    self.response.out.write(out)



#def main():
#  application = webapp.WSGIApplication([('/', MainPage)],debug=True)
#  wsgiref.handlers.CGIHandler().run(application)

#if __name__ == "__main__":
#  main()

print __name__
#print request
print webapp.RequestHandler
#print self.__name__