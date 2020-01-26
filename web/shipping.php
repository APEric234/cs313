
<html>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script src="cart.js"></script>
<body>

<h1>Shipping</h1>
<form action="confirm.php" method="post">
    You are ordering Red Paint: <input type="number" name="red" value = "<?php echo $_POST["red"];?>" readonly><br>
    
    You are ordering Green Paint: <input type="number" name="green" value = "<?php echo $_POST["green"];?>" readonly><br>
    You are ordering Blue Paint: <input type="number" name="blue" value = "<?php echo $_POST["blue"];?>" readonly><br>
    You are ordering Yellow Paint: <input type="number" name="yellow" value = "<?php echo $_POST["yellow"];?>" readonly><br>
    Please provide your shipping address: <input type="text" name="address">
    <p>Push submit to confirm your address</p>
    <input type="submit">
</body>
</html>
