<?php
// Start the session
session_start();
?>
<!DOCTYPE html> 
<html>
<body>

<h1>Products</h1>

<?php
$colors = array("red", "green", "blue", "yellow");

foreach ($colors as $value) {
  echo "$value <br>";
}
?>


</body>
</html>
