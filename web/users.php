
<?php
require_once('db.php')
?>
<html>
  <head>
<link rel="stylesheet" href="users.css">
</head>
<body>

<h1>Welcome Players!</h1>

<ul>
<?php
$db = get_db();


  
$query = 'select * from users;';
$stmnt = $db->query($query);
$stmnt -> execute();
$users = $stmnt->fetchAll();
foreach ($users as $user){
  $id=$user['user_id'];
  $namep=$user['fname'];

  echo("<li>Meet <b>$namep</b></li>");
}

?>
</ul>


<p class="stats">New player looking to be added</p>
<form method="post" action="success_player.php">
    <label for="name">Name:</label>
    <input type="text" name="name" id="name" value = "" required>
    <label for="users_id">Email:</label>
    <input type="text" name="email" id="email" value = "" required><br>
    </br>
    <input type="submit" name="add_user" id="add_user">
</body>
<footer><a href="characters.php"> Want to check what characters have already been made?</a></footer>
</html>