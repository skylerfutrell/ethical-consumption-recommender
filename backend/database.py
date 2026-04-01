from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# This creates your second SQL database file
engine = create_engine("sqlite:///./ethics_recommender.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Brand(Base):
    __tablename__ = "brands"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    category = Column(String)  # e.g., 'Apparel', 'Tech', 'Food'
    ethics_score = Column(Float) # 0.0 to 5.0
    description = Column(String)

# Build the table
Base.metadata.create_all(bind=engine)