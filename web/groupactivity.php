
create table scriptures

<html>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script src="cart.js"></script>
<body>

<h1>Order Confirmation</h1>

<?php $red=$_POST["red"];
 if ($red > 0){
  echo "<p>You ordered $red gallons of red paint</p>";
}?>
<?php $green=$_POST["green"];
if ($red > 0){
  echo "<p>You ordered $green gallons of green paint</p>";
}?>
<?php $blue=$_POST["blue"];
if ($red > 0){
  echo "<p>You ordered $blue gallons of blue paint</p>";
}?>
<?php $yellow=$_POST["yellow"];
if ($red > 0){
  echo "<p>You ordered $yellow gallons of yellow paint</p>";
}?>
    <P> We will ship your order to <?php 
    echo htmlspecialchars($_POST["address"])
    ?></p>
</body>
</html>
