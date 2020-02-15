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
    $users_id=$_post['users_id'];
    $query = "select User_id from characters where User_id = $id;";
    if(len($id_duplicate) == 1){

      $stmnt = $db->query($query);
      $stmnt -> execute();
      $id_duplicate = $stmnt->fetchAll();

      $name=$_POST['name'];
      
      $agility=$_POST['agil'];
      $strength=$_POST['stre'];
      $wisdom=$_POST['wisd'];
      $intel=$_POST['intel'];
      $grace=$_POST['grace'];

      $query2 = "insert  into characters (Character_id,Fname,Users_id,Agil,Stre,Wisd,Intel,Grace) Values($id,$agility,$strength,$wisdom,$intel,$grace);";
      echo '
        <html><body>
        <b> Your hero $name has been added to the list of characters succesfully!<b>
        <a href="characters.php"> Click here to go back and see him on the list of hero\'s!</a>
  
        </body></html>
      ';
    }
    else{
      echo '
        <html><body>
        <b> Your hero couldn\'t be added to the list of characters due to an error with the user_id you gave<b>
        <a href="characters.php"> Click here to go back and try again</a>
      
        </body></html>
        ';
    }
   
  
?> 