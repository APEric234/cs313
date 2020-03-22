function getAllMedicines(){
  //get all topics
  var result={medicines: [{"tylenol":1},
  {"advile":2},
  {"bilirubin":3},
  {"summer flu":4}]};
  return result;

}
function getMedicineId(num){
  var result={"great medicine":num};
  return result;
  //get all topics
}
function insertNewMedicine(name){
  //inserts to db
  var results = {succes:true}
  return results;

}
module.exports = {getMedicineId:getMedicineId,
  insertNewMedicine:insertNewMedicine,
  getAllMedicines,getAllMedicines

}