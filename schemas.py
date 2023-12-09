import datetime as _dt
import pydantic as _pydantic
import uuid


class _BaseHttp(_pydantic.BaseModel):
    ip: str
    method: str
    uri: str
    status: int


class Http(_BaseHttp):
    id: int
    date_created: _dt.datetime

    class Config:
        from_attributes = True


class CreateHttp(_BaseHttp):
    pass
