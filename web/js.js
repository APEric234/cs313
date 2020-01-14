$(function(){(".click").click(function(){
  $(this).innerHTML = "Clicked!";
})
});

$(function(){(".color").click(function(){
  $('.a1').css("background-color", $('.colorInput').innerHtml)
})
});

$(function(){(".visibility").click(function(){
  $('.a3').fadeOut(2500)
})
});