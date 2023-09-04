from fastapi import FastAPI
from typing import List
from models import User,Gender,Role
from uuid import uuid4

app=FastAPI()

db:List[User]=[
    User(
         id=uuid4(),
         first_name="Melos",
         last_name="Mulu",
         middle_name="Simeneh",
         gender=Gender.male,
         roles=[Role.admin,Role.user]
         )
]

@app.get("/")
def root():
    return {"Hello World"}

@app.get("/api/users")
async def fetch_users():
    return db