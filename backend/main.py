from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

## cors fix
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

todos =  ["Buy groceries", "Read a book", "Go for a walk"]

@app.get("/")
def read_root():
    return {"text": "Hello World"}

class TodoItem(BaseModel):
    todo: str

@app.post("/todos")
def add_todo(todo: TodoItem):
    todos.append(todo.todo)
    return {"message": "Todo added successfully", "todos": todos}

@app.get("/todos")
def get_todos():
    return {"todos": todos}


@app.get("/todos/{todo_id}")
def read_todo(todo_id: int):
     todo_id -= 1
     if 0 <= todo_id < len(todos):
        return {"todo": todos[todo_id]}
     else:
        return {"error": "Todo not found"}
     
