from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Simple Todo API")

class Todo(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False


todos = []

@app.get("/todolist")
def get_todos():
    return todos

@app.post("/todolist")
def add_todo(todo: Todo):
    todos.append(todo)
    return todo

# Delete a todo
@app.delete("/todolist/{todo_id}")
def delete_todo(todo_id: int):
    global todos
    todos = [t for t in todos if t.id != todo_id]
    return {"message": f"Todo {todo_id} deleted"}
