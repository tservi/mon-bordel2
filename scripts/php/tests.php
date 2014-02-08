<html>
<head></head>
<body>
<?php

function catchVal($s='',$begin='<',$end='>')
{
	$ret=$s;
	$posBegin=strpos($s,$begin);
	$posEnd=strpos($s,$end);
	if($posBegin>=0 and $posEnd>=0 and $posBegin<=$posEnd) 
	{
		$val='';
		if($posBegin>=0)
			{$val.=substr($s,0,$posBegin);}
		if($posEnd>0)
		{
			if(strlen($s)>$posEnd+1)
				{$val.=substr($s,$posEnd+1);}
			$ret=catchVal($val);
			print "ret=".$ret."<br/>\n";
		}	
	}
	return $ret;
}

$test='<tr><td align="left" width=50>Bla bla bla </td></tr>>>><<>';

//print $test;
print catchVal($test);
//$zLen=strlen($test);
//print(strpos($test,'>'));
//print(strstr($test,'>'));
//print substr_compare($test,'<',0);
/*
for($i=0;$i<$zLen;$i++)
{print $test[$i];}
*/
//print $test.search('<');

?>
</body>
</html>
