
<html>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script src="cart.js"></script>
<body>

<h1>Cart</h1>
<p class="yellow">You have purchased <?php echo $_POST["yellow"];?> yellow paint </p><button class="remove" id="yellow">Remove the yellow paint from your cart?</button>
<p class="green">You have purchased <?php echo $_POST["green"];?> green paint </p><button class="remove" id="green">Remove the green paint from your cart?</button>
<p class="red">You have purchased <?php echo $_POST["red"];?> red paint </p><button class="remove" id="red">Remove the red paint from your cart?</button>
<p class="blue">You have purchased <?php echo $_POST["blue"];?> blue paint </p> <button class="remove" id=" blue">Remove the blue paint from your cart?</button>
<a href="products.html">Back to Paint Store</a>
</body>
</html>
