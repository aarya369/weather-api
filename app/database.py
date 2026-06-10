from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#This is used for creating database tables through Python classes:
from sqlalchemy.orm import declarative_base


#How do I talk to PostgreSQL?

DATABASE_URL = (
    "postgresql://postgres:postgres@db:5432/weatherdb"
)
#Creates the pathway: Python 
#   ↓
#SQLAlchemy
#  ↓
#PostgreSQL
engine = create_engine(DATABASE_URL)
#just prepares the connection machinery.
#Actual connection often happens when the first query runs.


#opens a database conversation.
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
#Every database model will inherit from this.

Base = declarative_base()
#Without it SQLAlchemy won't know which classes are database tables.