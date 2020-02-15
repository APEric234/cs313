
<?php
require_once('db.php')
?>
<html>
  <head>
<link rel="stylesheet" href="characters.css">
</head>
<body>

<h1>Characters enter the field</h1>


<?php
$db = get_db();


  
$query = 'select * from characters;';
$stmnt = $db->query($query);
$stmnt -> execute();
$names = $stmnt->fetchAll();
echo("<ul>");
foreach ($names as $name){
  $namep=$name['fname'];
  echo("<li class='hero'>The Epic <b>$namep</b> has entered the game </li>");
}
echo("<\ul>");

?>



<p>Does anyone new enter the field?</p>
<form method="post" action="success.php">
    <label for="name">Name:</label>
    <input type="text" name="name" id="name" value = "" required><br>
    <label for="name">Users Id:</label>
    <input type="number" name="users_id" id="users_id" value = "" required><br>
    <label for="agil">Agility:</label>
    <input type="number" id="agil" name="agil" min="0" max="18" step="1" value="10">
    <label for="stre">Strength:</label>
    <input type="number" id="stre" name="stre" min="0" max="18" step="1" value="10">
    <label for="wisd">WisdoM:</label>
    <input type="number" id="wisd" name="wisd" min="0" max="18" step="1" value="10">
    <label for="intel">Intelligence:</label>
    <input type="number" id="intel" name="intel" min="0" max="18" step="1" value="10">
    <label for="grace">Grace:</label>
    <input type="number" id="grace" name="grace" min="0" max="18" step="1" value="10">
    <input type="submit" name="addCharacter" id="addCharacter">
</body>
</html>