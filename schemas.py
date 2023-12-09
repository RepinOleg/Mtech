import datetime as _dt
import pydantic as _pydantic


class _BaseHttp(_pydantic.BaseModel):
    ip: str
    http_method: str
    uri: str
    http_status: int


class Http(_BaseHttp):
    id: int
    date_created: _dt.datetime

    class Config:
        orm_mode = True


class CreateHttp(_BaseHttp):
    pass
