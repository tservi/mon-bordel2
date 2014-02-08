<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head></head>
<body>
<p>Lockers :</p>
<p>Logiweb qui permet de v&eacute;rouiller ou d&eacute;v&eacute;rouiller une clef</p>
<p>Verouillage sur des r&eacute;pertoires -> dirLock</p>
<p>Verouillage sur des fichiers -> fileLock</p>
<p>Verouillage sur des s&eacute;maphores -> semLock</p>
<p>Verouillage sur des fichiers -> popenLock</p>
<?php

/* test unitaire */
include_once('objects.php');
/* tester dirLock */
echo "<br/>\nTesting ... <br/>\n";
$clef="ceciEstUnTest";
$locking=new dirLock($clef);
$locking->lock();
echo "Status = ".($locking->status( )?"OK":"NOK")."<br/>\n";
$locking->unlock();
echo "Status = ".($locking->status( )?"OK":"NOK")."<br/>\n";
/* tester fileLock */
$locking=new fileLock($clef);
$locking->lock();
echo "Status = ".($locking->status( )?"OK":"NOK")."<br/>\n";
$locking->unlock();
echo "Status = ".($locking->status( )?"OK":"NOK")."<br/>\n";
/* tester semLock */
$locking=new semLock($clef);
$locking->lock();
echo "Status = ".($locking->status( )?"OK":"NOK")."<br/>\n";
$locking->unlock();
echo "Status = ".($locking->status( )?"OK":"NOK")."<br/>\n";
/* tester popenLock */
$locking=new popenLock($clef);
$locking->lock();
echo "Status = ".($locking->status( )?"OK":"NOK")."<br/>\n";
$locking->unlock();
echo "Status = ".($locking->status( )?"OK":"NOK")."<br/>\n";

?>

</body>
</html>