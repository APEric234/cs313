<?php
require_once('db.php')
?>

<?php
    $db=get_db();
    $id=rand(0,1000);
    
    $query = "select Character_id from characters where Character_id = $id;";


    $stmnt = $db->query($query);
    $stmnt -> execute();
    $id_duplicate = $stmnt->fetchAll(); 
    while(!empty($id_duplicate)){
      //note to self this will infinite loop once all 1000 are made need to fix later
      $id=rand();
      
      $query = "select Character_id from characters where Character_id = $id;";


      $stmnt = $db->query($query);
      $stmnt -> execute();
      $id_duplicate = $stmnt->fetchAll(); 
    }

    $users_id=$_POST['users_id'];

    $query = "select User_id from users where User_id = $users_id;";
    $stmnt = $db->query($query);
    $stmnt -> execute();
    $id_duplicate = $stmnt->fetchAll(); 
    if(!empty($id_duplicate)){

      $stmnt = $db->query($query);
      $stmnt -> execute();
      $id_duplicate = $stmnt->fetchAll();

      $name=$_POST['name'];
      
      $agility=$_POST['agil'];
      $strength=$_POST['stre'];
      $wisdom=$_POST['wisd'];
      $intel=$_POST['intel'];
      $grace=$_POST['grace'];

      $query2 = "insert  into characters (Character_id,Fname,Users_id,Agil,Stre,Wisd,Intel,Grace) Values($id,'$name',$users_id,$agility,$strength,$wisdom,$intel,$grace);";
      $stmnt = $db->query($query2);
      $stmnt -> execute();
      echo("
        <html><body>
        <b> Your hero $name has been added to the list of characters succesfully!<b>
        <a href=\"characters.php\"> Click here to go back and see him on the list of hero's!</a>
  
        </body></html>
      ");
    }
    else{
      echo("
        <html><body>
        <b> Your hero $name couldn't be added to the list of characters due to an error with the user_id you gave<b>
        <a href=\"characters.php\"> Click here to go back and try again</a>
      
        </body></html>
        ");
    }
   
  
?> 