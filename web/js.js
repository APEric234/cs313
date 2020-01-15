$(function(){
  $(".click").click(function(){
    $(".click").html( "Clicked!");
});

  $(".color").click(function(){
  $('.a1').css("background-color", "purple")
});


  $(".visibility").click(function(){
  $('.a3').fadeOut(2500)
  $('.a3').fadeIn(2500)
});

});