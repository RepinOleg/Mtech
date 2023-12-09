import datetime as _dt
import sqlalchemy as _sql
import uuid
import database as _database
from sqlalchemy.dialects.postgresql import UUID


class Http(_database.Base):
    __tablename__ = "http"
    id = _sql.Column(
        UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4
    )
    ip = _sql.Column(_sql.String, index=True)
    http_method = _sql.Column(_sql.String, index=True)
    uri = _sql.Column(_sql.String, index=True)
    http_status = _sql.Column(_sql.Integer, index=True)
    date_created = _sql.Column(
        _sql.TIMESTAMP(timezone=True), nullable=False, server_default=_sql.text("now()")
    )
