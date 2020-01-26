$(function(){
  $(".remove").click(function(){
    var theId = this.id;
    var b= document.getElementsByClassName(theId);
    b[0].style.display = "none";
    this.style.display = "none";

  
});

});
