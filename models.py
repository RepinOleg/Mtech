import datetime as _dt
import sqlalchemy as _sql

import database as _database


class Http(_database.Base):
    __tablename__ = "http"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    ip = _sql.Column(_sql.String, index=True)
    http_method = _sql.Column(_sql.String, index=True)
    uri = _sql.Column(_sql.String, index=True)
    http_status = _sql.Column(_sql.Integer, index=True)
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
