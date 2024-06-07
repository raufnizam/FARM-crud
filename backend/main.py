from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model import Todo
from database import (
    create_todo, fetch_all_todos, fetch_one_todo, remove_todo, update_todo
)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173", 
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Ping": "Pong"}

@app.get("/api/todo", response_model=list[Todo])
async def get_todos():
    response = await fetch_all_todos()
    return response    

@app.get("/api/todo/{title}", response_model=Todo)
async def get_todo_by_title(title: str):
    response = await fetch_one_todo(title)
    if response:
        return response
    else:
        raise HTTPException(404, f'Todo with title "{title}" not found')

@app.post("/api/todo", response_model=Todo)
async def post_todo(todo: Todo):
    response = await create_todo(todo.dict())
    if response:
        return response
    else:
        raise HTTPException(400, "There was an error / Bad request")

@app.put("/api/todo/{title}", response_model=Todo)
async def put_todo(title: str, description: str):
    response = await update_todo(title, description)
    if response:
        return response
    else:
        raise HTTPException(404, f'Todo with title "{title}" not found')

@app.delete("/api/todo/{title}")
async def delete_todo(title: str):
    response = await remove_todo(title)
    if response:
        return {"message": "Successfully deleted todo!"}
    else:
        raise HTTPException(404, f'Todo with title "{title}" not found')
