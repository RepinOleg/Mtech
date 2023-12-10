from datetime import datetime
from pydantic import BaseModel


class _BaseHttp(BaseModel):
    ip: str
    http_method: str
    uri: str
    http_status: int


class Http(_BaseHttp):
    id: int
    date_created: datetime

    class Config:
        orm_mode = True


class CreateHttp(_BaseHttp):
    pass
