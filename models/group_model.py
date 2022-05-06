from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship, backref
from config.db import db
from sqlalchemy.sql.schema import ForeignKey



class GroupModel(db.Model):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    name = Column(String(127), nullable=False)
    users = relationship("users", backref=backref("users"))
    admin = Column(Integer, ForeignKey("users.id"), nullable=False)


    


