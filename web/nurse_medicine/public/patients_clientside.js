function searchById(){
console.log("searchByID");
var id = $("#id").val();
console.log("Id: " + id);
$.get("/patient",{id:id}, function(data) {
  console.log("back from server with: " + data);
  console.log(data);
  var string = "<li>"
  for(var prop in data){
    string = string + prop + data[prop];
  }
  $("#patients").append(string + "</li>");
})
};

function getAllPatients(){
  $.get("/patients", function(data) {
    console.log("back from server with: " + data);
    var list =data["patients"];
    console.log(list);
    for (var x in list){

      y = list[x]
      for (var z in y){
        console.log(z);
        console.log(x);
      $("#patients").append("<li> " + z + " </li>");
      }
    }
  })
  };