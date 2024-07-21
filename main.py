# >uvicorn main:app --reload  # for automate reload after change in code
# http://127.0.0.1:8000/docs - здесь все ручки


from typing import Optional, Annotated
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from contextlib import asynccontextmanager

from db import create_tables, delete_tables
from router import tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('db cleared')
    await create_tables()
    print('db ready')
    yield
    print('db off')


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)



tasks = []



if __name__ == "__main__":

    pass
