# from fastapi import FastAPI

# app = FastAPI()
# @app.get("/hello")
# def hello():
#  return {"message": "Hello, World!"}

 # app/main.py
from fastapi import FastAPI, HTTPException, status
from .schemas import User, UserUpdate

app = FastAPI()
users: list[User] = []

@app.get("/api/users")
def get_users():
    return users

@app.get("/api/users/health", status_code=status.HTTP_200_OK)
def get_users():
    return {"Status": "ok"}

@app.get("/api/users/{user_id}")
def get_user(user_id: int):
    for u in users:
        if u.user_id == user_id:
            return u
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

@app.post("/api/users", status_code=status.HTTP_201_CREATED)
def add_user(user: User):
    if any(u.user_id == user.user_id for u in users):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="user_id already exists")
    users.append(user)
    return user

@app.put("/api/users/{user_id}", status_code=status.HTTP_200_OK)
def update_user(user_id: int, updated_user: User):

    for i, u in enumerate(users):
        if u.user_id == user_id:
            users[i].name = updated_user
        return updated_user

@app.delete("/api/users/{user_id}")
def delete_user(user_id: int): 
    users.pop(user_id)
    return {"message": "User deleted successfully"}
