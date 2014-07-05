<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<title>Obtenir la latitude et la longitude de l'adresse grâce à google maps api</title>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>
 <script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?sensor=false"></script>
<script type="text/javascript">
var geocoder;
geocoder = new google.maps.Geocoder();
function decode(){
    geocoder.geocode( { 'address': document.getElementById("adresse").value }, function(results, status)
            {
                if (status == google.maps.GeocoderStatus.OK)
                {
                    alert("Situation : " + results[0].geometry.location.lat() + " " +results[0].geometry.location.lng()); 
                }
                else
                {
                    alert("Erreur " + status);
                }
            }
        )
    }
 </script>
</head>
<body>
    <h1>Obtenir la latitude et la longitude de l'adresse grâce à google maps api</h1>
<input type="text" id= "adresse" name="adresse">
<input id="btn" type="button" value="Trouver " onclick="decode()"/>
</body>
</html>