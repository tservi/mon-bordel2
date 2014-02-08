<?php
/*
**********************************************************************************************************************************************
Auteur : Jean Tinguely Awais aka t-servi.com
- pas de licence - pas de copyright - heureux de l'avoir ecrit -
But : faire un listing des repertoires contenu dans le repertoire
**********************************************************************************************************************************************
*/

if($handle = opendir('.'))
{
	 echo "Liste des paquets : <br/>\n";
    while (false !== ($file = readdir($handle)))
	{
		if(is_dir($file) && $file!='.' && $file!='..' && $file!='.svn')
	        {echo '<a href="'.$file.'">'.$file.'</a> <br/>'."\n";}
    }
}

?>