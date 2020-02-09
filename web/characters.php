

<html>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script src="cart.js"></script>
<body>

<h1>Order Confirmation</h1>


<html>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script src="cart.js"></script>
<body>
<?php 


$dbUrl = getenv('DATABASE_URL');
$dbOpts = parse_url($dbUrl);
$dbHost = $dbOpts["host"];
$dbPort = $dbOpts["port"];
$dbUser = $dbOpts["user"];
$dbPassword = $dbOpts["pass"];
$dbName = ltrim($dbOpts["path"],'/');
$db = new PDO("pgsql:host=$dbHost;port=$dbPort;dbname=$dbName", $dbUser, $dbPassword);
echo "<h2> $db is </h2>";
?>
<h1>Order Confirmation</h1>
</body>
</html>

</body>
</html>
