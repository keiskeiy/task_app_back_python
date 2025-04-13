from fastapi import APIRouter
from model.Task import Task, TaskList
from api.route.todo import all_todo

router = APIRouter()


@router.get('/{todo_id}/alltasks', description="タスクをリスト形式で取得")
async def get_task(todo_id: str):
    # 一旦一時処理で仮のタスクを返す
    if not all_todo.get(todo_id):
        return []
    return all_todo[todo_id]


@router.post('/{todo_id}/tasks/{task_title}', description="タスクを追加")
async def create_task(task_title: str, todo_id: str):
    if all_todo.get(todo_id):
        all_todo[todo_id].append(Task(title=task_title))
    else:
        all_todo[todo_id] = [Task(title=task_title)]
    return all_todo[todo_id]


@router.delete('/{todo_id}/tasks/{task_title}', description="タスクを削除")
async def delete_task(task_title: str, todo_id: str):
    if all_todo.get(todo_id):
        all_todo[todo_id].remove(Task(title=task_title))
        return all_todo[todo_id]
    return []
