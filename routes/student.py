from fastapi import APIRouter
from fastapi import status
from typing import Optional
from utils import (
    add_data,
    get_records,
    get_record,
    update_record,
    delete_record
)
from schema.models import (
    CreateStudentRequest,
    CreateStudentResponse,
    ListStudentResponse,
    UpdateStudentResponse
)

router = APIRouter()

@router.post("/students", status_code=status.HTTP_201_CREATED, response_model=CreateStudentResponse)
async def create_students(request:CreateStudentRequest):
    """
    Create a new student.

    Args:
        request (CreateStudentRequest): The request body containing the student details.

    Returns:
        CreateStudentResponse: The response containing the ID of the created student.
    """
    student_id = await add_data(request.dict())
    return CreateStudentResponse.parse_obj({"id": student_id})

@router.get("/students", status_code=status.HTTP_200_OK, response_model=ListStudentResponse)
async def list_students(country: Optional[str] = None, age: Optional[int] = None):
    """
    Get a list of students.

    Args:
        country (str, optional): Filter students by country. Defaults to None.
        age (int, optional): Filter students by age. Defaults to None.

    Returns:
        ListStudentResponse: The response containing the list of students.
    """
    records = await get_records(country, age)
    for record in records:
        record.pop('_id', None)
    return ListStudentResponse.parse_obj({"data": records})

@router.get("/students/{id}",status_code=status.HTTP_200_OK, response_model=CreateStudentRequest)
async def fetch_student(id:str):
    """
    Get a student by ID.

    Args:
        id (str): The ID of the student.

    Returns:
        CreateStudentRequest: The response containing the student details.
    """
    record = await get_record(id)
    return CreateStudentRequest.parse_obj(record)

@router.patch("/students/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_student(id:str, request:CreateStudentRequest):
    """
    Update a student by ID.

    Args:
        id (str): The ID of the student.
        request (CreateStudentRequest): The request body containing the updated student details.

    Returns:
        None
    """
    await update_record(id, request.dict())
    return {}

@router.delete("/students/{id}", status_code=status.HTTP_200_OK, response_model=UpdateStudentResponse)
async def delete_student(id:str):
    """
    Delete a student by ID.

    Args:
        id (str): The ID of the student.

    Returns:
        UpdateStudentResponse: An Empty dictionary.
    """
    await delete_record(id)
    return UpdateStudentResponse