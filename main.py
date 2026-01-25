from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

# MySQL connection
engine = create_engine(
    "mysql+pymysql://root:password@localhost:3306/college",
    echo=True
)

Base = declarative_base()

# Table model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)

# Create table if not exists
Base.metadata.create_all(engine)
