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
foreach ($b as $c){
    echo ("<p>$c costs 1 <button class="$c">Buy</button></p>");

}?>


</body>
</html>
