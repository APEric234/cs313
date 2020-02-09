
<html>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script src="cart.js"></script>
<body>

<h1>Order Confirmation</h1>


<html>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script src="cart.js"></script>
<body>

<h1>Order Confirmation</h1>

<?php 
$conn_string = $db_connection = pg_connect(
  "host=localhost port=5432 dbname=dergo389khd0pd"
);
$conn = pg_pconnect($conn_string);
if (!$conn) {
    echo "An error occurred. here\n";
    exit;
}

$result = pg_query($conn, "SELECT * FROM equipment");
if (!$result) {
    echo "An error occurred. 2 here\n";
    exit;
}

$arr = pg_fetch_all($result);

print_r($arr);

?>
    <P> We will ship your order to <?php 
    echo htmlspecialchars($_POST["address"])
    ?></p>
</body>
</html>

</body>
</html>
