<?php
require_once('db.php')
?>

<?php
    $db=get_db();
    $id=rand(0,1000);
    
    $query = "select User_id from users where User_id = $id;";


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

    $name=htmlspecialchars($_POST['name']);
    
    $email=htmlspecialchars($_POST['email']);
    if (strpos($email,"@") !== false && (strpos($email,".") !== false && strpos($email,".") > strpos($email,"@")){
      $query2 = "insert  into users (Character_id,Fname,Email) Values($id,'$name',$email);";
      $stmnt = $db->query($query2);
      $stmnt -> execute();
      echo "
        <html><body>
        <b> Your hero $name has been added to the list of characters succesfully!<b>
        <a href=\"characters.php\"> Click here to go back and see him on the list of hero's!</a>

        </body></html>
      ";
    }

    
  
    else{
      echo "
        <html><body>
        <b> Your hero $name couldn't be added to the list of characters due to an error with the user_id you gave<b>
        <a href=\"characters.php\"> Click here to go back and try again</a>
      
        </body></html>
        ";
    }
   
  
?> 