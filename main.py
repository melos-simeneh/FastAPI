from fastapi import FastAPI,HTTPException
from typing import List
from models import User,Gender,Role,UserUpdateRequest
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

@app.put("/api/users/{id}")
async def update_user(user_update:UserUpdateRequest,id):
    for user in db:
        if user.id==id:
            if user_update.first_name is not None:
               user.first_name=user_update.first_name
            if user_update.last_name is not None:
               user.last_name=user_update.last_name
            if user_update.middle_name is not None:
               user.middle_name=user_update.middle_name
            if user_update.roles is not None:
               user.roles=user_update.roles
            return user
    
    raise HTTPException(status_code=404,detail= f"User with id {id} not found")

@app.delete("/api/users/{id}")
async def delete_user(id:UUID):
    for user in db:
     if user.id==id:
        db.remove(user)
        return 
    
    raise HTTPException(status_code=404,detail= f"User with id {id} not found")
    