from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime
#"What does our table look like?"
from app.database import Base
#With:class WeatherData(Base):SQLAlchemy understands: This class represents a database table.
#Python version of SQL table
class WeatherData(Base):
#blueprint for the database table.
    __tablename__ = "weather_data"

    id = Column(Integer, primary_key=True)

    city = Column(String)

    latitude = Column(Float)

    longitude = Column(Float)

    timestamp = Column(DateTime)

    temperature = Column(Float)

    created_at = Column(DateTime)