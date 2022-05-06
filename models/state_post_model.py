from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship, backref
from config.db import db
from sqlalchemy.sql.schema import ForeignKey
from datetime import date
from sqlalchemy.sql.sqltypes import Date


class PostsModel(db.Model):
    __tablename__ = "state"
    id = Column(Integer, primary_key=True)
    signed = relationship("users", backref=backref("users"))
    progress = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
