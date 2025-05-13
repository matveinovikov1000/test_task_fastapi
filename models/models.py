from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class URL(Base):
    """Модель URL"""
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, nullable=False, index=True)
    short_url = Column(String(10), unique=True, index=True, nullable=False)
