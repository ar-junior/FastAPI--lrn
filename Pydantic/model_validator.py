from pydantic import BaseModel, Field, EmailStr, model_validator
from typing import Optional, List, Dict

# data
patient_info = {
    "name" : "Arjun",
    "age" : 65,
    "email" : "arjun@oksbi.com" , 
    "allergies" : ["bukhar"],
    "contact_details" : {"phone":"63555555","emergency":"108"}
}

# model schema
class Patient(BaseModel):
    name : str 
    age : int
    email : str
    allergies : Optional[List[str]] = Field(default=None, max_length=1)
    contact_details : Dict[str, str]

    @model_validator(mode="after")
    def validate_emergency_contact(cls,model):
        if model.age > 60 and "emergency" not in model.contact_details :
            raise ValueError ("patients older then 60 must have an emergency contact")
        return model

# model object
patient1 = Patient(**patient_info)


# function 
def insert_patient(data : Patient):
    print(data.name)
    print(data.age)
    print(data.allergies)

# function call
insert_patient(patient1)
