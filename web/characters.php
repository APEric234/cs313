
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
#$conn_string = "host=ec2-184-72-236-3.compute-1.amazonaws.com database=dergo389khd0pd user=kxgzangzhzkpdm port=5432 password=c29f98a332d055f61fc092dbfef16a865ee78b843444b8846dfc3d60fb1c19f4"
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
