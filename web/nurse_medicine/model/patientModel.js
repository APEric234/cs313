function getAllPatients(){
  //get all topics
  var result={patients: [{"billly bob":1},
  {"billly joe bob":2},
  {"billly joe":3},
  {"billly sue":4}]};
  return result;

}
function getPatientById(num){
  var result={"billly bob":num};
  return result;
  //get all topics
}
function insertNewPatient(name){
  //inserts to db
  var results = {succes:true}
  return results;

}
module.exports = {getAllPatients:getAllPatients,
  getPatientById:getPatientById,
  insertNewPatient,insertNewPatient

}