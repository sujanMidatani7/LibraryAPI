from pydantic import BaseModel
from typing import List

class Address(BaseModel):
    """
    Represents the address of a student.
    """
    city: str
    country: str

class CreateStudentRequest(BaseModel):
    """
    Represents the request payload for creating a student.
    """
    name: str
    age: int
    address: Address

class CreateStudentResponse(BaseModel):
    """
    Represents the response payload for creating a student.
    """
    id: str

class ListStudent(BaseModel):
    """
    Represents a student in the list.
    """
    name: str
    age: int
    
class ListStudentResponse(BaseModel):
    """
    Represents the response payload for listing students.
    """
    data: List[ListStudent]

class UpdateStudentResponse(BaseModel):
    """
    Represents the response payload for updating a student.
    """
    pass

