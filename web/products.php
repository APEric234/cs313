<?php
// Start the session
session_start();
?>
<!DOCTYPE html> 
<html>
<body>

<h1>Products</h1>
=
<?php
$colors = array("red", "green", "blue", "yellow");

foreach ($colors as $value) {
  $class=$value;
  echo "$value <br>";
  echo "<button class=\"$class\">Buy</button>";
}
?>


</body>
</html>
