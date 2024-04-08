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
    student_id = await add_data(request.dict())
    return CreateStudentResponse.parse_obj({"id": student_id})

@router.get("/students", status_code=status.HTTP_200_OK, response_model=ListStudentResponse)
async def list_students(country: Optional[str] = None, age: Optional[int] = None):
    records = await get_records(country, age)
    for record in records:
        record.pop('_id', None)
    return ListStudentResponse.parse_obj({"data": records})

@router.get("/students/{id}",status_code=status.HTTP_200_OK, response_model=CreateStudentRequest)
async def fetch_student(id:str):
    record = await get_record(id)
    return CreateStudentRequest.parse_obj(record)

@router.patch("/students/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_student(id:str, request:CreateStudentRequest):
    await update_record(id, request.dict())
    return {}
    

@router.delete("/students/{id}", status_code=status.HTTP_200_OK, response_model=UpdateStudentResponse)
async def delete_student(id:str):
    await delete_record(id)
    return UpdateStudentResponse