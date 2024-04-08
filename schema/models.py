from pydantic import BaseModel
from typing import List

class Address(BaseModel):
    city:str 
    country: str

class CreateStudentRequest(BaseModel):
    name: str
    age: int
    address: Address

class CreateStudentResponse(BaseModel):
    id: str

class ListStudent(BaseModel):
    name: str
    age:int
    
class ListStudentResponse(BaseModel):
    data: List[ListStudent]

class UpdateStudentResponse(BaseModel):
    pass

