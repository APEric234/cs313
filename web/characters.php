
<?php
require_once('db.php')
?>
<html>
<body>

<h1>Characters enter the field</h1>


<?php
$db = get_db();


  
$query = 'select * from characters;';
$stmnt = $db->query($query);
$stmnt -> execute();
$names = $stmnt->fetchAll();

foreach ($names as $name){
  $namep=$name['fname'];
  echo("<p class='hero'>The Epic <b>$namep</b> has entered the game </p>");
}


?>

<?php
  if(isset($_POST['addCharacter'])) { 
    $id=rand(0,1000)
    
    $query = "select Character_id from characters where Character_id = $id;";


    $stmnt = $db->query($query);
    $stmnt -> execute();
    $id_duplicate = $stmnt->fetchAll(); 
    while(len($id_duplicate) > 0){
      //note to self this will infinite loop once all 1000 are made need to fix later
      $id=rand()
      
      $query = "select Character_id from characters where Character_id = $id;";


      $stmnt = $db->query($query);
      $stmnt -> execute();
      $id_duplicate = $stmnt->fetchAll(); 
    }
    $users_id=$_post['users_id']
    $query = "select User_id from characters where User_id = $id;";
    if(len($id_duplicate) == 1){

      $stmnt = $db->query($query);
      $stmnt -> execute();
      $id_duplicate = $stmnt->fetchAll();

      $name=$_POST['name']
      
      $agility=$_POST['agil']
      $strength=$_POST['stre']
      $wisdom=$_POST['wisd']
      $intel=$_POST['intel']
      $grace=$_POST['grace']

      $query2 = "insert  into characters (Character_id,Fname,Users_id,Agil,Stre,Wisd,Intel,Grace) Values($id,$agility,$strength,$wisdom,$intel,$grace);";
      header("Location: success.php");
    }
    else{
      header("Location: fail.php");
    }
  } 
  
?> 

<p>Does anyone new enter the field?</p>
<form method="post">
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
    <input type="submit" name="addCharacter" >
</body>
</html>