from sqlalchemy import Column, String,Integer
from database.database import Base

class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
