import json
from pathlib import Path
DB=Path("todos.json")
def load_todos():
  if DB.exists():
    return json.loads(DB.read_text(encoding="utf-8"))
  return[]
def save_todos(todos):
  DB.write_text(json.dumps(todos,indent=2),encoding="utf-8")
def add_todo(text):
  todos=load_todos()
  todos.append({"task":text,"done":False})
  save_todos(todos)
def list_todos():
  for i,t in enumerate(load_todos(),1):
    mark="✓" if t.get("done")else " "
    print(f"{i}. [{mark}] {t.get('task')}")
def remove_todo(index):
  todos=load_todos()
  if 1<=index<=len(todos):
    todos.pop(index-1)
    save_todos(todos)
def mark_done(index):
  todos=load_todos()
  if 1<=index<=len(todos):
    todos[index-1]["done"]=True
    save_todos(todos)
