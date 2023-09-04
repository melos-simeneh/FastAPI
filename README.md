# FastAPI-CRUD-Operations
## Prerequisites
1. FastAPI basics
2. Python installed
## Install Dependencies
1. fastAPI
2. uvicorn
```
$ pip install fastapi uvicorn
```
## Run server
```
$ uvicorn main:app --reload
```
this will start the app on http://127.0.0.1:8000 \
swagger doc http://127.0.0.1:8000/docs

## API Endpoints
- GET **/api/users**: Get all users
- POST **/api/user**: Create user
- GET **/api/users/:id**: Get a user
- PUT **/api/users/:id**: Update a user.
- DELETE **/api/users/:id**: Delete a user.
## Thank You
Thank you for taking the time to explore the Todo app. I hope it provides you with valuable information.
