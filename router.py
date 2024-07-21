from typing import Annotated

from fastapi import APIRouter, Depends

from repository import TasksRepository
from schemas import STaskAdd, STask

tasks_router = APIRouter(
    prefix="/tasks",
    tags=["Таски"],
)

@tasks_router.post("")
async def add_task(
    task: Annotated[STaskAdd, Depends()],

):

    #tasks.append(task)
    task_id = await TasksRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


@tasks_router.get("/all")
async def get_tasks() -> list[STask]:
    tasks_l = await TasksRepository.find_all()
    return tasks_l