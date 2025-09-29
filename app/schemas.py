# app/schemas.py
from pydantic import BaseModel, EmailStr, constr, conint

class User(BaseModel):
 user_id: int
 name: constr(min_length=2, max_length=50)
 email: EmailStr #normal email sontraints
 age: conint(gt=18) #>18
 student_id: constr(pattern=r'^S\d{7}$') #must start with "S" and follwed by exaclty 7 digits

class UserUpdate(BaseModel):
    user_id: int
    name: constr(min_length=2, max_length=50)
    email: EmailStr
    age: conint(gt=18)
