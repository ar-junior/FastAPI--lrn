from pydantic import BaseModel, Field, field_validator, EmailStr
from typing import Optional, List

# data
patient_info = {
    "name" : "Arjun",
    "age" : 21,
    "email" : "arjun@oksbi.com" , 
    "allergies" : ["bukhar"]
}

# model schema
class Patient(BaseModel):
    name : str
    age : int
    email : str
    allergies : Optional[List[str]] = Field(default=None, max_length=1)

    # field validation
    @field_validator('email')
    @classmethod
    def email_validator (cls,value):
        valid_domain = ["oksbi.com", "bob.com"]

        # abc@email.com
        domain_name = value.split("@")[-1]
        if domain_name in valid_domain:
            return value
        raise ValueError ("Not a valid domain")

    # field transform 
    @field_validator("name")
    @classmethod
    def name_transform(cls, value):
        return value.upper()

# model object
patient1 = Patient(**patient_info)


# function
def insert_patient(data : Patient):
    print(data.name)
    print(data.age)
    print(data.allergis)

# function call
insert_patient(patient1)

