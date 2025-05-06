from sqlalchemy import Column, String, Float, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TransactionORM(Base):
    __tablename__ = "transactions"

    id = Column(String, primary_key=True, index=True)
    category = Column(String)
    amount = Column(Float)
    date = Column(Date)
    type = Column(String)  # "income" or "expense"
    recurring = Column(String)  # Stores "No", "Daily", etc.