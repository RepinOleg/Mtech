from typing import TYPE_CHECKING, List

import database as _database
import models as _models
import schemas as _schemas

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


def _add_tables():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def create_http(http: _schemas.CreateHttp, db: "Session") -> _schemas.Http:
    http_model = _models.Http(**http.model_dump())
    db.add(http_model)
    db.commit()
    db.refresh(http_model)
    return _schemas.Http(
        id=http_model.id,
        ip=http.ip,
        http_method=http.method,
        uri=http.uri,
        http_status=http.status,
        date_created=http_model.date_created,
    )


async def get_all_http(db: "Session") -> List[_schemas.Http]:
    http = db.query(_models.Http).all()
    return list([_schemas.Http.model_dump(http)])
