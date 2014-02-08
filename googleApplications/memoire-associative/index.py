# code source de
# http://memoire-associative.appspot.com/
#


import cgi
import wsgiref.handlers
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext import db

class pageAcceuil(webapp.RequestHandler):
  def get(self):
    rep=''
    rep+=formulaireRecherche
    rep+=formulaireInsertion
    self.response.out.write(enteteHtml+enteteCorpsHtml+rep+finCorpsHtml+finHtml)

class recherche(webapp.RequestHandler):
    def post(self):
     rep=''
     rep+=formulaireRecherche
     laRequete=cgi.escape(self.request.get('requete'))
     rep+=cartoucheDessus
     rep+='<table style="width:400px">'
     rep+='<tr><td>Votre demande : "'+laRequete+'"</td></tr>\n'
     requeteTable=str(laRequete).split(' ')
     maRequete = db.GqlQuery("Select * from memoireAssociative ")
     mesResultats = maRequete.fetch(maRequete.count())
     quantite=0
     texte=''
     for r in mesResultats:
        trouve={}
        for t in requeteTable:
          trouve[t]=False
        mesClefs=['clef','contexte','version','valeur']
        for c in mesClefs:
         for t in requeteTable:
          if str(eval("r."+c)).find(t)>=0:
           trouve[t]=True
        toutTrouve=True
        for k in trouve:
         if trouve[k]==False:
          toutTrouve=False
        if toutTrouve:
         quantite+=1
         texte+="<tr><td>\n"
         texte+='<hr/>'
         texte+="<table width='100%'>\n"
         for c in mesClefs:
          texte+="<tr><td>"+str(c)+"</td><td>"+str(eval("r."+c))+"</td></tr>\n"
         texte+="</table>"
         texte+="</td></tr>\n"
     rep+="<tr><td>Il y a "+str(quantite)+" r&eacute;sultat(s) pour votre demande </td></tr>\n"
     rep+=texte
     rep+='</table>\n'
     rep+=cartoucheDessous
     self.response.out.write(enteteHtml+enteteCorpsHtml+retourAcceuil+rep+finCorpsHtml+finHtml)

class insere(webapp.RequestHandler):
    def post(self):
     rep=''
     #rep+=formulaireInsertion
     mesClefs=['clef','contexte','valeur']
     dictionnaire={}
     for c in mesClefs:
      dictionnaire[c]=cgi.escape(self.request.get(c))
     rep+=cartoucheDessus
     rep+='<table style="width:400px">'
     rep+='<tr><td>Vos donn&eacute;es</td></tr>\n'
     for v in dictionnaire.values():
      rep+='<tr><td style="align-text:left;">'
      rep+='"'+v+'"'
      rep+='</td></tr>\n'
     maRequete = db.GqlQuery("Select * from memoireAssociative ")
     mesResultats = maRequete.fetch(maRequete.count())
     lastVersion=0.0
     for r in mesResultats:
      found=True
      for k in ['clef','contexte']:
       if not found or not eval("r."+k)==dictionnaire[k]:
        found=False
      if found:
       lastVersion=r.version+1.0
     if lastVersion==0.0:
      rep+="<tr><td>Sont une nouvelle entr&eacute;e</td></tr>\n"
     else:
      rep+="<tr><td>Sont une nouvelle version : version "+str(int(lastVersion))+" cr&eacute;e. </td></tr>\n"
     rep+='</table>\n'
     monEnregistrement=memoireAssociative(clef=dictionnaire['clef'],contexte=dictionnaire['contexte'],version=lastVersion,valeur=dictionnaire['valeur'])
     monEnregistrement.put()
     rep+=cartoucheDessous
     self.response.out.write(enteteHtml+enteteCorpsHtml+retourAcceuil+rep+finCorpsHtml+finHtml)

class creationXml(webapp.RequestHandler):
    def get(self):
     	 maRequete = db.GqlQuery("Select * from memoireAssociative ")
	 mesResultats = maRequete.fetch(maRequete.count())
	 clef=''
	 contexte=''
	 if(cgi.escape(self.request.get('clef'))):
	  clef=cgi.escape(self.request.get('clef'))
	 if(cgi.escape(self.request.get('contexte'))):
	  contexte=cgi.escape(self.request.get('contexte'))
	 fichierXml=""
	 fichierXml+='<?xml version="1.0" encoding="utf-8"?>\n'
	 fichierXml+='<enregistrements>'
	 for r in mesResultats:
	  if (r.clef.find(clef)>=0 and r.contexte.find(contexte)>=0):
	   fichierXml+="<enregistrement>\n"
	   fichierXml+="<clef><![CDATA["+str(r.clef)+"]]></clef>\n"
	   fichierXml+="<contexte><![CDATA["+str(r.contexte)+"]]></contexte>\n"
	   fichierXml+="<version><![CDATA["+str(r.version)+"]]></version>\n"
	   fichierXml+="<valeur><![CDATA["+str(r.valeur)+"]]></valeur>\n"
	   fichierXml+="</enregistrement>\n"
	 fichierXml+='</enregistrements>'
	 self.response.headers["Content-Type"] = "text/xml"
	 self.response.out.write(fichierXml)


def racine():
  application = webapp.WSGIApplication(
                                       [('/', pageAcceuil),
                                        ('/recherche', recherche),
                                        ('/insere', insere),
										('/xml', creationXml)
                                        ],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)



class memoireAssociative(db.Model):
    clef=db.TextProperty()
    contexte=db.TextProperty()
    version=db.FloatProperty()
    valeur=db.TextProperty()

hauteurBordureCartouche=32
largeurBordureCartouche=32
largeurCartouche=650
cartoucheDessus="""
<table cellspacing="0" cellpadding="0" border="0" align="center" width="%s">
<tr>
<td height="%s" width="%s" style="background: transparent url(img/cartouche/top-left.png) repeat-y scroll top left; width: %spx; height: %spx;"> </td>
<td height="%s" width="%s" style="background: transparent url(img/cartouche/border-top.png) repeat-x scroll top left ; width: %spx; height: %spx;"> </td>
<td height="%s" width="%s" style="background: transparent url(img/cartouche/top-right.png) no-repeat scroll top left; width: %spx; height: %spx;"> </td>
</tr>

<tr>
<td height="100%s" style="background: transparent url(img/cartouche/border-left.png) repeat-y scroll top left; height: 100%s;"> </td>

<td align="center" class="interieurCartouche">

"""%((hauteurBordureCartouche+largeurBordureCartouche+largeurCartouche),hauteurBordureCartouche,largeurBordureCartouche,largeurBordureCartouche,hauteurBordureCartouche,hauteurBordureCartouche,largeurCartouche,largeurCartouche,hauteurBordureCartouche,hauteurBordureCartouche,largeurBordureCartouche,largeurBordureCartouche,hauteurBordureCartouche,'%','%')

cartoucheDessous="""
</td>

<td height="100%s"  style="background: transparent url(img/cartouche/border-right.png) repeat-y scroll top left;"> </td>
</tr>

<tr>
<td height="%s" style="background: transparent url(img/cartouche/bottom-left.png) repeat-y scroll top left; height: %spx;"> </td>
<td height="%s" style="background: transparent url(img/cartouche/border-bottom.png) repeat-x scroll top left; height: %spx;"> </td>
<td height="%s" style="background: transparent url(img/cartouche/bottom-right.png) repeat-y scroll top left; height: %spx;"> </td>
</tr>
</table>

"""%('%',hauteurBordureCartouche,hauteurBordureCartouche,hauteurBordureCartouche,hauteurBordureCartouche,hauteurBordureCartouche,hauteurBordureCartouche)

retourAcceuil="""
%s
<a href="/">Retour a la page principale</a><br/>
%s
"""%(cartoucheDessus,cartoucheDessous)

enteteHtml="""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html lang="fr">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-15" />
<title>Memoire associative</title>

<style type="text/css">
<!--
.corpsHtml { background:#000000 url(img/bg.png) repeat scroll 0 0; margin:0px;color:white}
.interieurCartouche {background:#cccccc;color:black;}
-->
</style>

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

	  xinha_editors = xinha_editors ? xinha_editors :
	  [
	    'valeur'
	  ];


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


</head>
"""

enteteCorpsHtml="""
<body class="corpsHtml">
%s
<b>Stocker et chercher des associations entre des mots en fonction d'un contexte</b>
%s
"""%(cartoucheDessus, cartoucheDessous)


finCorpsHtml="""
<br/>
<br/>
%s
 cr&eacute;&eacute; par <a href="http://www.t-servi.com">http://www.t-servi.com</a> - sans garanties - sans but lucratif - code source de l'appliction <a href="http://www.t-servi.com/cgi-bin/trac.cgi/browser/googleApplications/memoire-associative">ici</a>
%s
</body>
"""%(cartoucheDessus, cartoucheDessous)


finHtml="""
</html>
"""

formulaireRecherche="""
%s
<div width="%s">
<br/>
<form action="recherche" method="post">
Entrez votre recherche et appuyez sur enter : <input type="text" name="requete" style="width:300px"/>
</form>
<br>
</div>
%s
"""%(cartoucheDessus,(hauteurBordureCartouche+largeurBordureCartouche+largeurCartouche), cartoucheDessous)


formulaireInsertion="""
%s
<form action="insere" method="post">
<table style="width:400">
<tr><td>
Votre clef :
</td></tr>
<tr><td>
<input type="text" name="clef" value="" style="width:400px;" />
</td></tr>
<tr><td>
Votre contexte :
</td></tr>
<tr><td>
<input type="text" name="contexte" value="" style="width:400px" />
</td></tr>
<tr><td>
Votre valeur :
</td></tr>
<tr><td>
<textarea name="valeur" id="valeur" style="width:400px;;height:250px;" ></textarea>
</td></tr>
<tr><td>
<input type="submit" />
<tr><td>
</table>
</form>
%s
"""%(cartoucheDessus, cartoucheDessous)

if __name__ == "__main__":
  racine()