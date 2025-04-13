from fastapi import APIRouter

import api.route.task as todos
from api.route import (todo, task)

api_router = APIRouter()

api_router.include_router(task.router, tags=["タスク管理API"])

api_router.include_router(todo.router, tags=["Todo管理API"])
