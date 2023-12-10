from typing import TYPE_CHECKING, List

import database
import models
import schemas

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


def _add_tables():
    return database.Base.metadata.create_all(bind=database.engine)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def create_http(http: schemas.CreateHttp, db: "Session") -> schemas.Http:
    http_model = models.Http(**http.model_dump())
    db.add(http_model)
    db.commit()
    db.refresh(http_model)
    return schemas.Http(
        id=http_model.id,
        ip=http.ip,
        http_method=http.http_method,
        uri=http.uri,
        http_status=http.http_status,
        date_created=http_model.date_created,
    )


async def get_http(db: "Session") -> schemas.Http:
    http_model = db.query(models.Http).all()

    return http_model
