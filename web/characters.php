

<html>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script src="cart.js"></script>
<body>

<h1>Order Confirmation</h1>


<?php 

function get_DB(){
  $db = null;
  try{
$dbUrl = getenv('DATABASE_URL');
$dbOpts = parse_url($dbUrl);
$dbHost = $dbOpts["host"];
$dbPort = $dbOpts["port"];
$dbUser = $dbOpts["user"];
$dbPassword = $dbOpts["pass"];
$dbName = ltrim($dbOpts["path"],'/');
$db = new PDO("pgsql:host=$dbHost;port=$dbPort;dbname=$dbName", $dbUser, $dbPassword);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
  }catch(PDOException $ex){
    echo "Error connecting to db. detalis: $ex"
  }
  return $db;
}


$db = get_db()
$query = 'select fname from characters';
$stmnt = $db->query($query);
$stmnt -> execute();
$names = $stmnt->fetchAll();

?>
<html>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script src="cart.js"></script>
<body>
<?php 
foreach ($names as $name){
  $namep=$name['fname'];
  echo("<p>The Epic <b>$namep</b> has entered the game </p>");
}
?>
