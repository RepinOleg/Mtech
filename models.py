import datetime as _dt
from sqlalchemy import Column, Integer, String, DateTime

import database as _database


class Http(_database.Base):
    __tablename__ = "http"
    id = Column(Integer, primary_key=True, index=True)
    ip = Column(String, index=True)
    http_method = Column(String, index=True)
    uri = Column(String, index=True)
    http_status = Column(Integer, index=True)
    date_created = Column(DateTime, default=_dt.datetime.utcnow)
