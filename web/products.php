<?php
// Start the session
session_start();
?>
<!DOCTYPE html> 
<html>
<body>

<h1>Products</h1>

<?php
$colors = array("red paint", "green paint", "blue paint", "yellow paint");

foreach ($colors as $value) {
  $class=$value;
  echo "$value <br>";
  echo "<button class=\"$class\">Buy</button><br>";
}
?>


</body>
</html>
