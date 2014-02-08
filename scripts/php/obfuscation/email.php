<html>
<head></head>
<body>

<div id="mailto">test&lt;at&gt;test.com</div>


<?php

$mailto='<a href="maito:test@test.com>tets@test.com</a>';
$rot=str_replace('"','\"',str_rot13($mailto));

?>
<script type="text/javascript">
<!-- 

myId=document.getElementById('mailto');
myId.innerHTML="<?php echo $rot; ?>".replace(/[a-zA-Z]/g, function(c){return String.fromCharCode((c<="Z"?90:122)>=(c=c.charCodeAt(0)+13)?c:c-26);});

-->
</script>


</body>
</html>