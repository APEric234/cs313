<?php
// Start the session
session_start();
?>
<!DOCTYPE html> 
<html>
<body>

<h1>Products</h1>

<?php
$_SESSION["favcolor"] = "green paint";
$a = $_SESSION["favcolor"];
$b=array($_SESSION["favcolor"],"yellow paint");
$d = array("0");
foreach ($b as $c){
  foreach($d as $price){
    echo ("<p>$c costs $price <button class="$c">Buy</button></p>"); 
  }

}?>


</body>
</html>
