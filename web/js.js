$(function(){
  $(".click").click(function(){
    $(".click").html( "Clicked!");
});

  $(".color").click(function(){
  $('.a1').css("background-color", $(".colorInput").val())
});


  $(".visibility").click(function(){
  if($('.a3').is(":visible")){

    $('.a3').fadeOut(2500)
    $(".visibility").html( "Make third div visible!")
    
  }else{
    $('.a3').fadeIn(2500)
    $(".visibility").html( "Make third div invisible!")
  
  }
});

});