from fastapi import FastAPI
from typing import List
from models import User,Gender,Role
from uuid import UUID,uuid4

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

@app.get("/api/users")
async def fetch_users():
    return db

@app.post("/api/users")
async def create_user(user:User):
    db.append(user)
    return user

@app.delete("/api/users/${id}")
async def delete_user(id:UUID):
    for user in db:
     if user.id==id:
        db.remove(user)
        return 
    