from sqlalchemy import Column, String, DateTime, Enum, Integer, UniqueConstraint, event
import datetime, bcrypt
from database import Base

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user = Column(Enum("user", "admin", name="user_roles"), nullable=False)
    email = Column(String(255), nullable=False, unique=True)  # Enforce unique email constraint
    _password = Column(String(255), nullable=False)
    created_date = Column(DateTime, nullable=False, default=datetime.datetime.now)
    updated_date = Column(DateTime, nullable=False, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    __table_args__ = (UniqueConstraint('email', name='uq_user_email'),)  # Optional: enforce unique email on table level

    def __str__(self):
        return self.user

    # Password property
    @property
    def password(self):
        return self._password
    
    # Setter to hash password before saving
    @password.setter
    def password(self, raw_password):
        hashed_password = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt())  # Hash the password
        self._password = hashed_password.decode('utf-8')  # Store the hashed password

    # Method to verify password
    def verify_password(self, raw_password):
        return bcrypt.checkpw(raw_password.encode('utf-8'), self._password.encode('utf-8'))

# Optionally handle creation and update timestamps with SQLAlchemy events
@event.listens_for(Users, 'before_insert')
def set_created_date(mapper, connection, target):
    target.created_date = datetime.datetime.now()

@event.listens_for(Users, 'before_update')
def set_updated_date(mapper, connection, target):
    target.updated_date = datetime.datetime.now()
