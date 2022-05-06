from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship, backref
from config.db import db
from sqlalchemy.sql.schema import ForeignKey
from datetime import date
from sqlalchemy.sql.sqltypes import Date


class PostsModel(db.Model):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    group = Column(String(127), nullable=False)
    autor = relationship("users", backref=backref("users"))
    signed = Column(Integer, ForeignKey("users.id"), nullable=False)
    progress = relationship("state", backref=backref("state"))
    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    date = Column(Date, nullable=False)

