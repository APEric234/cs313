
<html>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script src="cart.js"></script>
<body>

<h1>Cart</h1>
<form action="shipping.php" method="post">
    You have Red Paint: <input type="number" name="red" value = "<?php echo $_POST["red"];?>" required><br>
    
    You have Green Paint: <input type="number" name="red" value = "<?php echo $_POST["green"];?>" required><br>
    You have Blue Paint: <input type="number" name="red" value = "<?php echo $_POST["blue"];?>" required><br>
    You have Yellow Paint: <input type="number" name="red" value = "<?php echo $_POST["yellow"];?>" required><br>
    <p>Push submit to confirm your cart</p>
    <input type="submit">
</body>
</html>
