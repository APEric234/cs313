<?php
// Start the session
session_start();
?>
<!DOCTYPE html> 
<html>
<body>

<h1>My first PHP page</h1>

<?php
$_SESSION["favcolor"] = "green";
$a = $_SESSION["favcolor"];
$b=array($_SESSION["favcolor"],"yellow");
foreach ($b as $c){
echo ("<p>Hello World your item costs $c </p>"); 
}?>

<form action="" method="post">
    Name:  <input type="text" name="personal[name]" /><br />
    Email: <input type="text" name="personal[email]" /><br />
    Beer: <br />
    <select multiple name="beer[]">
        <option value="warthog">Warthog</option>
        <option value="guinness">Guinness</option>
        <option value="stuttgarter">Stuttgarter Schwabenbräu</option>
    </select><br />
    <input type="submit" value="submit me!" />
</form>

</body>
</html>
