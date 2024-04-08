from config.db import DB
import uuid

async def add_data(data):
    """
    Add data to the library database.

    Args:
        data (dict): The data to be added.

    Returns:
        str: The ID of the added data.
    """
    mongo = DB()
    client = mongo.client

    data['id'] = str(uuid.uuid4())
    client.Library.students.insert_one(data)
    return data['id']

async def get_records(country=None, age=None):
    """
    Get records from the library database based on optional filters.

    Args:
        country (str, optional): The country to filter the records by.
        age (int, optional): The minimum age to filter the records by.

    Returns:
        list: A list of student records matching the filters.
    """
    client = DB().client
    query = {}
    if country:
        query['address.country'] = country
    if age:
        query['age'] = {'$gte': age}
    records = client.Library.students.find(query, projection={'_id': False})
    students = []   
    for record in records:
        students.append(record)
    return students

async def get_record(id:str):
    """
    Get a single record from the library database based on ID.

    Args:
        id (str): The ID of the record to retrieve.

    Returns:
        dict: The record matching the given ID.
    """
    client = DB().client
    record = client.Library.students.find_one({'id': id}, projection={'_id': False, 'id': False})
    return record

async def update_record(id, data):
    """
    Update a record in the library database.

    Args:
        id (str): The ID of the record to update.
        data (dict): The updated data for the record.

    Returns:
        None
    """
    client = DB().client
    client.Library.students.update_one({'id': id}, {'$set': data})

    return

async def delete_record(id):
    """
    Delete a record from the library database.

    Args:
        id (str): The ID of the record to delete.

    Returns:
        int: The number of records deleted (should be 0 or 1).
    """
    client = DB().client
    result = client.Library.students.delete_one({'id': id})
    return result.deleted_count


