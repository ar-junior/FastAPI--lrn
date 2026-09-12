from pydantic import BaseModel, Field, field_validator, EmailStr
from typing import Optional, List, Dict

# data
patient_info = {
    "name" : "Arjun",
    "age" : 21,
    "email" : "arjun@oksbi.com" , 
    "allergies" : ["bukhar"],
    "contact_details" : {"phone":"63555555","emr":"001"}
}

# model schema
class Patient(BaseModel):
    name : str
    age : int
    email : str
    allergies : Optional[List[str]] = Field(default=None, max_length=1)
    contact_details : Dict[str, str]

# model object
patient1 = Patient(**patient_info)


# function
def insert_patient(data : Patient):
    print(data.name)
    print(data.age)
    print(data.allergis)

# function call
insert_patient(patient1)

