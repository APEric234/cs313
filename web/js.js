$(function(){
  $(".click").click(function(){
  $(this).innerHTML = "Clicked!";
});

  $(".color").click(function(){
  $('.a1').css("background-color", $('.colorInput').innerHtml)
});


  $(".visibility").click(function(){
  $('.a3').fadeOut(2500)
});

});