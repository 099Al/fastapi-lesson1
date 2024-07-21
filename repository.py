from sqlalchemy import select

from db import new_session, TaskOrm
from schemas import STaskAdd, STask


class TasksRepository:
    @classmethod
    async def add_one(clf, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def find_all(clf):
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            tasks_schemas = [STask.model_validate(task_model) for task_model in task_models]
            return tasks_schemas
