$(function(){
  $(".click").click(function(){
    $(".click").html( "Clicked!");
});

  $(".color").click(function(){
  $('.a1').css("background-color", $('.colorInput').html())
});


  $(".visibility").click(function(){
  $('.a3').fadeOut(2500)
});

});