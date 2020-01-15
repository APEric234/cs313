$(function(){
  $(".click").click(function(){
    $(".click").html( "Clicked!");
});

  $(".color").click(function(){
  $('.a1').css("background-color", $(".colorInput").val())
});


  $(".visibility").click(function(){
  b=0
  if($('.a3').css('display') == "None"){
    $('.a3').fadeIn(2500)
    $(".visibility").html( "Make third div invisible!")
    b=1
  }else{
  if (b == 0 ){
    $('.a3').fadeOut(2500)
    $(".visibility").html( "Make third div visible!")
  }
  }
});

});