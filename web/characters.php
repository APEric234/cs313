

<html>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script src="cart.js"></script>
<body>

<h1>Order Confirmation</h1>

<?php 
require('db.php');
$db = get_db()
$query = 'select fname from characters'
$stmnt = $db->prepare($query);
$names = $stmnt->fetchAll(PDO::FETCH_ASSOC);
?>
<html>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script src="cart.js"></script>
<body>
<?php 
foreach ($names as $name){
  $namep=$name['fname'];
  echo("<p>The Epic <b>$namep</b> has entered the game </p>")
}
?>
