function searchById(){
console.log("searchByID");
var id = $("#id").val();
console.log("Id: " + id);
$.get("/medicine",{id:id}, function(data) {
  console.log("back from server with: " + data);
  console.log(data);
  var string = "<li>"
  for(var prop in data){
    string = string + prop + data[prop];
  }
  $("#medicine").append(string + "</li>");
})
};

function getAllMedicines(){
  $.get("/medicines", function(data) {
    console.log("back from server with: " + data);
    var list =data["medicines"];
    console.log(list);
    for (var x in list){

      y = list[x]
      for (var z in y){
        console.log(z);
        console.log(x);
      $("#medicine").append("<li> " + z + " </li>");
      }
    }
  })
  };