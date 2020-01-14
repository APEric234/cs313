$(function(){(".button").click(function(){
  $(this).innerHTML = "Clicked!";
})
});

$(function(){("button2").click(function(){
  $('.a1').css("background-color", $('.colorInput').innerHtml)
})
});