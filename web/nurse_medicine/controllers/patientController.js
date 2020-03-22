const patientModels = require("../model/patientModel");
function allPatients(req,res){
  //get all patients
  console.log("getting all patients");
  var result=patientModels.getAllPatients();
  res.json(result);
  }
function singlePatient (req,res){
  //.id will pull  1 for a url with ?id=1
  var id =req.query.id
  console.log("getting single patient with id: " + id);
  var result = patientModels.getPatientById(id)
res.json(result);
};
function addPatient (req,res) {
  var name = req.body.name;
  console.log("creating a new patient with name: " + name);
  var result = patientModels.insertNewPatient(name);
  res.json(result);
};
module.exports = {
  addPatient:addPatient,
  singlePatient:singlePatient,
  allPatients:allPatients
};