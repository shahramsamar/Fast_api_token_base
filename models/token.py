from sqlalchemy import Column, String,Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base

class TokenModel(Base):
    __tablename__ = "tokens"
    id = Column(Integer, primary_key=True, autoincrement=True)
    token = Column(String, nullable=False, index=True)
    expiration_date = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User",back_populates="tokens")