from typing import TYPE_CHECKING, List
from fastapi import FastAPI
import fastapi as _fastapi
import sqlalchemy.orm as _orm

import schemas as _schemas
import services as _services

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

app = _fastapi.FastAPI()


@app.post("/api/", response_model=_schemas.Http)
async def create_http(
    http: _schemas.CreateHttp,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    return await _services.create_http(http=http, db=db)


@app.get("/api/", response_model=List[_schemas.Http])
async def get_http(db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return await _services.get_all_http(db=db)
