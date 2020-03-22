const express = require("express");
const path = require("path");

const medicineController = require("./controllers/medicineController")
const patientController = require("./controllers/patientController")
var app = express();
const PORT = process.env.PORT || 5000;
app.use(express.static(path.join(__dirname,"public")));
app.use(express.urlencoded({extended:true}));//support url encoded body
app.use(express.json());
app.get("/patients",patientController.allPatients);
app.get("/patient",patientController.singlePatient);
app.post("/patient",patientController.addPatient);
app.get("/medicines",medicineController.allMedicines);
app.get("/medicine",medicineController.singleMedicine);
app.post("/medicine",medicineController.addMedicine);

app.listen(PORT, function() {
  console.log("Server lisetning on port " + PORT);
});