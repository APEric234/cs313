const medicineModel = require("../model/medicineModel");
function allMedicines(req,res){
  //get all patients
  console.log("getting all medicines");
  var result=medicineModel.getAllMedicines();
  res.json(result);
  }
function singleMedicine (req,res){
  //.id will pull  1 for a url with ?id=1
  var id =req.query.id
  console.log("getting single medicine with id: " + id);
  var result = medicineModel.getMedicineId(id);
res.json(result);
};
function addMedicine (req,res) {
  var name = req.body.name;
  console.log("creating a new medicine with name: " + name);
  var result = medicineModel.insertNewMedicine(name);
  res.json(result);
};
module.exports = {
  addMedicine:addMedicine,
  singleMedicine:singleMedicine,
  allMedicines:allMedicines
};