
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
    echo $text;?>
    
    You are ordering Green Paint: <input type="number" name="red" value = "<?php echo $_POST["green"];?>" readonly><br>
    You are ordering Blue Paint: <input type="number" name="red" value = "<?php echo $_POST["blue"];?>" readonly><br>
    You are ordering Yellow Paint: <input type="number" name="red" value = "<?php echo $_POST["yellow"];?>" readonly><br>
    Your shipping address is : <input type="text" name="address">
    <p>Push submit to confirm your address</p>
    <input type="submit">
</body>
</html>
