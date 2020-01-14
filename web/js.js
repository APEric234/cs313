$(function(){(".button").click(function(){
  $(this).innerHTML = "Clicked!";
}
function colorchange(){
  document.getElementsByClassName("a1")[0].style.backgroundColor = document.getElementsByClassName("colorInput")[0].value
}