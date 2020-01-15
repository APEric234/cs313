$(function(){
  $(".click").click(function(){
    $(".click").html( "Clicked!");
});

  $(".color").click(function(){
  $('.a1').css("background-color", $(".colorInput").val())
});


  $(".visibility").click(function(){
  if($('.a3').is(":visible")){
    window.alert("is visible")

    $('.a3').fadeOut(2500)
    $(".visibility").html( "Make third div visible!")
    
  }else{
    window.alert("isn't visible")
    $('.a3').fadeIn(2500)
    $(".visibility").html( "Make third div invisible!")
  
  }
});

});