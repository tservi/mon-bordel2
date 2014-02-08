<?php
function loadFileIfExist($f)
{if(file_exists($f)){include $f;}}

//session_start();
$allFiles=Array('mvc/views/html/doctype.html','mvc/controllers/html.php');
// fichier index
$indexFile='files.index.txt';
if(!file_exists($indexFile))
	{
		$f=fopen($indexFile,'w+');
		fwrite($f,'1000');
	}
// fichier zip
$zip = new ZipArchive();
$zipName='files.indexed.zip';
$creation=false;
if(!file_exists($zipName))
	{$creation=$zip->open($zipName, ZIPARCHIVE::CREATE);}
else
	{$creation=$zip->open($zipName);}
$zip->addFromString(time().".testfilephp.txt" , "#1 Ceci est un test, ajouté en tant que fichier testfilephp.txt.\n");
$zip->close();
$myHead=<<<HereDoc
<head>
<title>
test
</title>
</head>

HereDoc;
$myBody=<<<HereDoc
<body>
<h1>Hello World</h1>
</body>

HereDoc;
for($i=0;$i<count($allFiles);$i++)
{loadFileIfExist($allFiles[$i]);}
?>