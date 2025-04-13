from fastapi import APIRouter
from model.Todo import Todo

all_todo = {}
router = APIRouter()


@router.post('/todos/{todo_id}', description="Todoリストを追加")
async def create_todo(todo_id: str):
    if todo_id in all_todo:
        print(f'already exists：{todo_id}')
    all_todo[todo_id] = []
    return list(all_todo.keys())


@router.get('/alltodos', description="Todoリストを取得")
async def get_todo():
    return list(all_todo.keys())


@router.delete('/todos/{todo_id}', description="Todoリストを削除")
async def delete_todo(todo_id: str):
    if todo_id in all_todo:
        del all_todo[todo_id]
        return all_todo
    return list(all_todo.keys())
