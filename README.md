
# LibraryAPI
This API is a simple student managment system. It allows you to add, delete, update and view students.

## Installation
1. Clone the repository
2. Run `python3.11 -m venv .venv` to create a virtual environment
3. Run `source .venv/bin/activate` to activate the virtual environment
4. Run `pip install poetry` to poetry dependency manager
5. Install dependencies by running `poetry install`
6. Run the application by running `uvicorn main:app --reload`
7. Open `https://libraryapi-h26h.onrender.com` in your browser to view the documentation which is deployed in render. If you are using localhost replace it with the IP address of your machine.

## Usage
The API has the following endpoints:
1. `/students` - GET, POST
2. `/students/{id}` - GET, PATCH, DELETE

## Dependencies
1. FastAPI
2. Uvicorn
3. Pydantic
4. Poetry
5. PyMongo


## Contributors
[Sujan Midatani](https://github.com/sujamiditani7)

## License
[MIT](https://choosealicense.com/licenses/mit/)


