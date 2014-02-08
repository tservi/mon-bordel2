# code source de
# http://aidemoi.appspot.com/
#


import cgi
import wsgiref.handlers

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext import db

class MainPage(webapp.RequestHandler):
  def get(self):
  	width=450
	height='80px'
	rep="""
<div>

%s
</div>

<div>

<form action="askHelp" method="post" enctype="multipart/form-data">
<script>
<!--
function testValRequest()
{
 ret=true;
 root='entry';
 zDiv='point';
 for(var i=1;i<6;i++)
  {
   myE=document.getElementById(root+i);
   if(myE.value.length<=0)
   	{
		document.getElementById(zDiv+i).style.backgroundColor='orange';
		ret=false;
	}
	else
	{
		document.getElementById(zDiv+i).style.backgroundColor='';
	}

  }
 return ret;
}
-->
</script>
%s
<b>Demander</b><br/>
Pour demander de l'aide, vous devez remplir une demande en 5 points : <br/><br/><br/>

<div style="text-align:left;width:%spx;">
<div id="point1">
Point 1 : Rentrez une adresse email de contact *
<br/>
<input type="text" id="entry1" name="email" style="width:%spx;" />
</div>
<div id="point2">
Point 2 : D&eacute;crivez la situation *
<br/>
<textarea id="entry2" name="situation" style="width:%spx;height:%s;"></textarea>
</div>
<div id="point3">
Point 3 : D&eacute;crivez les sentiments face &agrave; la situation *
<br/>
<textarea id="entry3" name="feelings" style="width:%spx;height:%s;"></textarea>
</div>
<div id="point4">
Point 4 : D&eacute;crivez les besoins *
<br/>
<textarea id="entry4" name="needs" style="width:%spx;height:%s;"></textarea>
</div>
<div id="point5">
Point 5 : Formulez une demande simple et concr&egrave;te *
<br/>
<textarea id="entry5" name="request" style="width:%spx;height:%s;"></textarea>
</div>
</div>
<input type="submit" value="Demander de l'aide" onclick="return testValRequest();">
<br/>
* champs obligatoires
%s

</form>
<br/>
</div>
    """%(myDoingHelp,cartoucheUp,width,width,width,height,width,height,width,height,width,height, cartoucheDown)
	self.response.out.write(myHeader+myBodyHeader+rep+myBodyFooter+myFooter)


class askingHelp(webapp.RequestHandler):
    def post(self):
 		rep=myHeader
		rep+=myBodyHeader
		rep+=cartoucheUp
		rep+='<a href="/">Retour a la page principale</a><br/>\n'
		rep+=cartoucheDown
		rep+=cartoucheUp
		rep+='Votre demande:<br/>\n'
		vals=[]
		myKeys=['email','situation','feelings','needs','request']
		allOk=True
		for k in myKeys:
			if self.request.get(k):
				myVal=cgi.escape(self.request.get(k))
				if len(myVal)<1:
					allOk=False
				vals.append(myVal)
			else:
				allOk=False
				vals.append('')
		if allOk:
			for v in vals:
				rep+='------------------------------------------------------<br/>\n'
				rep+=v
				rep+='<br/>\n'
			rep+='Est enregistr&eacute;e.<br/><br/>'
		else:
			rep+="Des donn&eacute;es manquent....<br/><br/>"
		rep+=cartoucheDown
		if allOk:
			myR=HelpRequest(email=vals[0], situation=vals[1], feelings=vals[2], needs=vals[3],request=vals[4])
			myR.put()
		rep+=myBodyFooter
		rep+=myFooter
		self.response.out.write(rep)


class doingHelp(webapp.RequestHandler):
    def post(self):
		zSearch=''
		if self.request.get('search'):
			zSearch=cgi.escape(self.request.get('search'))
		rep=myHeader
		rep+=myBodyHeader
		rep+=cartoucheUp
		rep+='<a href="/">Retour a la page principale</a><br/>\n'
		rep+=cartoucheDown
		rep+=myDoingHelp
		queryRequest = db.GqlQuery("Select * from HelpRequest ")
		result=queryRequest.fetch(queryRequest.count())
		myTxt=""
		myCount=0
		for r in result:
			if r.request.find(zSearch)>=0 or r.situation.find(zSearch)>=0 or r.feelings.find(zSearch)>=0 or r.needs.find(zSearch)>=0 :
				myCount+=1
				myTxt+="""
			%s
			<div style="width:100%s;text-align:left">
			Situation:<br/>
			%s
			<br/>
			Sentiments:<br/>
			%s
			<br/>
			Besoins:<br/>
			%s
			<br/>
			Demande:<br/>
			%s
			<br/>
			<a href="mailto:%s" >
			Envoyer un email a cette personne par le client mail
			</a>
			<br/>
			</div>
			%s
			"""%(cartoucheUp,'%',r.situation,r.feelings,r.needs,r.request,r.email,cartoucheDown)
		rep+=cartoucheUp
		rep+='Votre recherche: '+zSearch+'<br/>\n'
		rep+='Quantit&eacute;e de r&eacute;sultats retourn&eacute;s : '+str(myCount)+' sur '+str(queryRequest.count())+'demandes.<br/>\n'
		rep+=cartoucheDown
		rep+=myTxt
		rep+=myBodyFooter
		rep+=myFooter
		self.response.out.write(rep)


def main():
  application = webapp.WSGIApplication(
                                       [('/', MainPage),
                                        ('/askHelp', askingHelp),
                                        ('/doHelp', doingHelp)],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)


# ------------------------------------------------------------------------------------
# Data handling
# ------------------------------------------------------------------------------------

class HelpRequest(db.Model):
    email=db.StringProperty()
    situation=db.TextProperty()
    feelings=db.TextProperty()
    needs=db.TextProperty()
    request=db.TextProperty()

cartoucheUp="""
<table cellspacing="0" cellpadding="0" border="0" align="center" width="564">
<tr>
<td height="32" width="47" style="background: transparent url(img/cartouche/top-left.png) repeat-y scroll 0% 0%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial; width: 47px; height: 32px;"> </td>
<td height="32" width="500" style="background: transparent url(img/cartouche/border-top.png) repeat-x scroll 0% 0%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial; width: 500px; height: 32px;"> </td>
<td height="32" width="32" style="background: transparent url(img/cartouche/top-right.png) no-repeat scroll 0% 0%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial; width: 32px; height: 32px;"> </td>
</tr>

<tr>
<td height="100%" width="47" style="background: transparent url(img/cartouche/border-left.png) repeat-y scroll 0% 0%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial; width: 47px; height: 100%;"> </td>

<td align="center">

"""

cartoucheDown="""
</td>

<td height="100%" width="32" style="background: transparent url(img/cartouche/border-right.png) repeat-y scroll 0% 0%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial; width: 32px;"> </td>
</tr>

<tr>
<td height="32" width="47" style="background: transparent url(img/cartouche/bottom-left.png) repeat-y scroll 0% 0%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial; width: 47px; height: 32px;"> </td>
<td height="32" width="716" style="background: transparent url(img/cartouche/border-bottom.png) repeat-x scroll 0% 0%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial; width: 716px; height: 32px;"> </td>
<td height="32" width="32" style="background: transparent url(img/cartouche/bottom-right.png) repeat-y scroll 0% 0%; -moz-background-clip: -moz-initial; -moz-background-origin: -moz-initial; -moz-background-inline-policy: -moz-initial; width: 32px; height: 32px;"> </td>
</tr>
</table>

"""


myHeader="""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html lang="fr">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-15" />
<title>Aide-moi</title>

  <script type="text/javascript">
    _editor_url  = "/xinha/"  // (preferably absolute) URL (including trailing slash) where Xinha is installed
    _editor_lang = "en";      // And the language we need to use in the editor.
    _editor_skin = "silva";   // If you want use a skin, add the name (of the folder) here
  </script>
  <script type="text/javascript" src="/xinha/XinhaCore.js"></script>

  <script>
  <!--
	xinha_editors = null;
	xinha_init    = null;
	xinha_config  = null;
	xinha_plugins = null;

	// This contains the names of textareas we will make into Xinha editors
	xinha_init = xinha_init ? xinha_init : function()
	{
	   /** STEP 1 ***************************************************************
	   * First, specify the textareas that shall be turned into Xinhas.
	   * For each one add the respective id to the xinha_editors array.
	   * I you want add more than on textarea, keep in mind that these
	   * values are comma seperated BUT there is no comma after the last value.
	   * If you are going to use this configuration on several pages with different
	   * textarea ids, you can add them all. The ones that are not found on the
	   * current page will just be skipped.
	   ************************************************************************/

	  /*
	  xinha_editors = xinha_editors ? xinha_editors :
	  [
	    'entry2', 'entry3', 'entry4', 'entry5'
	  ];
	  */

	  xinha_editors = xinha_editors ? xinha_editors :
	  [];

	  /** STEP 2 ***************************************************************
	   * Now, what are the plugins you will be using in the editors on this
	   * page.  List all the plugins you will need, even if not all the editors
	   * will use all the plugins.
	   *
	   * The list of plugins below is a good starting point, but if you prefer
	   * a simpler editor to start with then you can use the following
	   *
	   * xinha_plugins = xinha_plugins ? xinha_plugins : [ ];
	   *
	   * which will load no extra plugins at all.
	   ************************************************************************/

	  xinha_plugins = xinha_plugins ? xinha_plugins :
	  [
	   'CharacterMap',
	   'ContextMenu',
	   'ListType',
	   'Stylist',
	   'Linker',
	   'SuperClean',
	   'TableOperations'
	  ];
	  xinha_plugins = xinha_plugins ? xinha_plugins :
	  [ ];

	         // THIS BIT OF JAVASCRIPT LOADS THE PLUGINS, NO TOUCHING  :)
	         if(!Xinha.loadPlugins(xinha_plugins, xinha_init)) return;


	  /** STEP 3 ***************************************************************
	   * We create a default configuration to be used by all the editors.
	   * If you wish to configure some of the editors differently this will be
	   * done in step 5.
	   *
	   * If you want to modify the default config you might do something like this.
	   *
	   *   xinha_config = new Xinha.Config();
	   *   xinha_config.width  = '640px';
	   *   xinha_config.height = '420px';
	   *
	   *************************************************************************/

	   xinha_config = xinha_config ? xinha_config() : new Xinha.Config();


	   // To adjust the styling inside the editor, we can load an external stylesheet like this
	   // NOTE : YOU MUST GIVE AN ABSOLUTE URL

	   xinha_config.pageStyleSheets = [ _editor_url + "examples/full_example.css" ];

	  /** STEP 4 ***************************************************************
	   * We first create editors for the textareas.
	   *
	   * You can do this in two ways, either
	   *
	   *   xinha_editors   = Xinha.makeEditors(xinha_editors, xinha_config, xinha_plugins);
	   *
	   * if you want all the editor objects to use the same set of plugins, OR;
	   *
	   *   xinha_editors = Xinha.makeEditors(xinha_editors, xinha_config);
	   *   xinha_editors.myTextArea.registerPlugins(['Stylist']);
	   *   xinha_editors.anotherOne.registerPlugins(['CSS','SuperClean']);
	   *
	   * if you want to use a different set of plugins for one or more of the
	   * editors.
	   ************************************************************************/

	  xinha_editors   = Xinha.makeEditors(xinha_editors, xinha_config, xinha_plugins);

	  /** STEP 5 ***************************************************************
	   * If you want to change the configuration variables of any of the
	   * editors,  this is the place to do that, for example you might want to
	   * change the width and height of one of the editors, like this...
	   *
	   *   xinha_editors.myTextArea.config.width  = '640px';
	   *   xinha_editors.myTextArea.config.height = '480px';
	   *
	   ************************************************************************/


	  /** STEP 6 ***************************************************************
	   * Finally we "start" the editors, this turns the textareas into
	   * Xinha editors.
	   ************************************************************************/

	  Xinha.startEditors(xinha_editors);
	}

	Xinha._addEvent(window,'load', xinha_init); // this executes the xinha_init function on page load
	                                            // and does not interfere with window.onload properties set by other scripts

  -->
  </script>

<style type="text/css">
<!--
.myBody { background:#FFFFFF url(img/bg.png) repeat scroll 0 0; margin:0px;}
-->
</style>
</head>
"""
myBodyHeader="""
<body class="myBody">
%s
<b>Offrir ou demander de l'aide.</b>
%s
"""%(cartoucheUp, cartoucheDown)

myBodyFooter="""
<br/>
<br/>
%s
 - cr&eacute;&eacute; par <a href="http://www.t-servi.com">http://www.t-servi.com</a> -
 <br/>
 - sans garanties - sans but lucratif -
 <br/>
 code source de l'appliction <a href="http://www.t-servi.com/cgi-bin/trac.cgi/browser/googleApplications/aidemoi">ici</a>
%s
</body>
"""%(cartoucheUp, cartoucheDown)

myDoingHelp="""
<form action="doHelp" method="post" enctype="multipart/form-data">

%s
<b>Donner</b><br/>
Pour offir de l'aide lancez une recherche et le programme trouvera certainement une demande d'aide qui remplira ce crit&egrave;re.
<br/><br/>
Mon crit&egrave;re pour offir de l'aide :
<input type="text" name="search" />
<input type="submit" value="chercher">
%s

</form>
"""%(cartoucheUp, cartoucheDown)

myFooter="""
</html>
"""
if __name__ == "__main__":
  main()