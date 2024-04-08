from config.db import DB
import uuid

async def add_data(data):
    mongo = DB()
    client = mongo.client

    data['id'] = str(uuid.uuid4())
    client.Library.students.insert_one(data)
    return data['id']

async def get_records(country=None, age=None):
    client = DB().client
    query = {}
    if country:
        query['country'] = country
    if age:
        query['age'] = {'$gte': age}
    records = client.Library.students.find(query,projection={'_id': False})
    students = []   
    for record in records:
        students.append(record)
    return students
   

async def get_record(id:str):
    client = DB().client
    record = client.Library.students.find_one({'id': id}, projection={'_id': False, 'id': False})
    return record

async def update_record(id, data):
    client = DB().client
    client.Library.students.update_one({'id': id}, {'$set': data})

    return

async def delete_record(id):
    client = DB().client
    result = client.Library.students.delete_one({'id': id})
    return result.deleted_count


