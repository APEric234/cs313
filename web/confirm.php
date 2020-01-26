
<html>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script src="cart.js"></script>
<body>

<h1>Cart</h1>
<?php $red=$_POST["red"];
if $red > 0{
  echo "<p>You ordered $red gallons of red paint</p>";
}?>
<?php $red=$_POST["green"];
if $red > 0{
  echo "<p>You ordered $red gallons of green paint</p>";
}?>
<?php $red=$_POST["blue"];
if $red > 0{
  echo "<p>You ordered $red gallons of blue paint</p>";
}?>
<?php $red=$_POST["yellow"];
if $red > 0{
  echo "<p>You ordered $red gallons of yellow paint</p>";
}?>
    <P> We will ship your order too <?php 
    $text=$_POST["address"];
    $text = preg_replace('/[^a-z0-9 ]+/','',$text);
    echo $text;?></p>
</body>
</html>
