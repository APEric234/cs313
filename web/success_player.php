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
      
      $query = "select User_id from users where User_id = $id;";


      $stmnt = $db->query($query);
      $stmnt -> execute();
      $id_duplicate = $stmnt->fetchAll(); 
    }

    $name=htmlspecialchars($_POST['name']);
    
    $email=htmlspecialchars($_POST['email']);
    if (strpos($email,"@") !== false && (strpos($email,".") !== false && strpos($email,".") > strpos($email,"@"))){
      print($id);
      
      try{
      $query2 = "insert  into users (User_id,Fname,Email) Values($id,'$name','$email');";
      $stmnt = $db->query($query2);
      $stmnt -> execute();
      echo "
        <html><body>
        <b> Your have been added as a user your id is $id please remember this so you can add a character later<b>
        <a href=\"characters.php\"> Click here to go and get a hero added for your user!</a>

        </body></html>
      ";
      }catch{
        echo "
        <html><body>
        <b> Your have already added as a user please refresh the page<b>
        <a href=\"characters.php\"> Click here to go and get a hero added for your user!</a>

        </body></html>
      ";
      }
    }


    
  
    else{
      echo "
        <html><body>
        <b> You couldn't be added as a user due to an invalid email<b>
        <a href=\"users.php\"> Click here to go back and try again</a>
      
        </body></html>
        ";
    }
   
  
?> 