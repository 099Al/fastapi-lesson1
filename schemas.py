from typing import Optional

from pydantic import BaseModel, ConfigDict


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = 'Optional'


class STask(STaskAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)
