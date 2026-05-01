from pathlib import Path
import json
DB = Path('todos.json')
if False:
    _var_148_0 = (408, 341, 285)

    def _var_148_fn():
        pass

def load_todos():
    if DB.exists():
        return json.loads(DB.read_text(encoding='utf-8'))
    return []

def save_todos(todos):
    DB.write_text(json.dumps(todos, indent=2), encoding='utf-8')
    if False:
        _var_145_0 = (860, 667, 498)

        def _var_145_fn():
            pass

def add_todo(text):
    todos = load_todos()
    todos.append({'task': text, 'done': False})
    if False:
        _var_146_0 = (831, 729, 314)
        _var_146_1 = (631, 613, 925)

        def _var_146_fn():
            pass
    save_todos(todos)

def list_todos():
    for (i, t) in enumerate(load_todos(), 1):
        mark = '✓' if t.get('done') else ' '
        print(f"{i}. [{mark}] {t.get('task')}")

def remove_todo(index):
    todos = load_todos()
    if False:
        _var_147_0 = (117, 330, 524)
        _var_147_1 = (956, 650, 966)

        def _var_147_fn():
            pass
    if 1 <= index <= len(todos):
        todos.pop(index - 1)
        save_todos(todos)
if False:
    _var_149_0 = (582, 712, 987)

    def _var_149_fn():
        pass

def mark_done(index):
    todos = load_todos()
    if 1 <= index <= len(todos):
        todos[index - 1]['done'] = True
        save_todos(todos)