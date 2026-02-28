import uuid
from sqlalchemy import Column, String, Integer, Float, Boolean, Text, Date, Numeric, JSONB
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase): pass

class PostgresData(Base):
    __tablename__ = "postgres_data"

    updated_at = Column(DateTime(timezone=True), default=func.now(), nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now(), nullable=False)
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    def __repr__(self):
        return f'<PostgresData {self.id}>'