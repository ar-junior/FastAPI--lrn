from fastapi import FastAPI, Path, HTTPException
import json
app = FastAPI()

def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)
    return data

# GET
@app.get("/") # home page
def hello():
    return {"message":"Patient Management System API"}

@app.get("/about") # about page
def about():
    return {"message":"A fully functional API to manage your patient records"}

@app.get("/view") # view patients recored list
def view_patients():
    data = load_data()
    return data

@app.get("/patient/{patient_id}") # view single patient using patient ID
def view_patient(patient_id : str = Path(..., description="id of the patient in DB", example="P001") ):
    # load all the patients
    data = load_data()

    if patient_id in data:
        patient = data[patient_id]
        return patient
    raise HTTPException (status_code=404, detail="patient not found")




# POST
# PUT
# DELETE
