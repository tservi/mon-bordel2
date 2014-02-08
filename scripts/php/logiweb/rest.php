<?php
/*
**********************************************************************************************************************************************
Auteur : Jean Tinguely Awais aka t-servi.com
- pas de licence - pas de copyright - heureux de l'avoir ecrit -
But : permettre de manipuler les logiweb grace a  des requetes HTTP
**********************************************************************************************************************************************
*/

$noPackage='No Package';
$noClass='No Class';
$noMethod='No Method';

if(isset($_REQUEST['new']) && strlen($_REQUEST['new'])>0 )
{
	/*
	instancier l'objet :
	j'ai besoin du nom du logiweb, de la classe, des parametres du constructeur, de la fonction a  appeler et des parametres de la fonction
	*/
	$new=$_REQUEST['new'];
	list($package, $object, $paramConstruct, $function, $params) =split("\.", $new,strlen($new));
	/*
	echo 'Package = '.$package."<br/>\n";
	echo 'Object = '.$object."<br/>\n";
	echo 'Constructeur = '.$paramConstruct."<br/>\n";
	echo 'Function = '.$function."<br/>\n";
	echo 'Params = '.$params."<br/>\n";
	*/
	if(file_exists($package.'/objects.php'))
	{
		include_once($package.'/objects.php');
		if(class_exists($object))
		{
			$o=new $object($paramConstruct);
			if(method_exists($object, $function ))
			{
				if (count($params)>0)
			 		{$o->$function($params);}
				else
					{$o->$function();}
				return $o->out;		// tous les logiweb doivent avoit une variable out!
			}
			else
				{return $noMethod;}
		}
		else
			{return $noClass;}
	}
	else
		{return $noPackage;}
}

?>