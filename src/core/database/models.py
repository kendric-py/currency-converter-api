from sqlalchemy import Column, String, Integer

from .base import Base



class Currency(Base):
    __tablename__ = 'currencies_list'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)