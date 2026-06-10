from fastapi import FastAPI, Depends, Query

from app.database import engine
from app.database import Base, SessionLocal
from app.models import WeatherData

from sqlalchemy.orm import Session

from app.schemas import WeatherRequest
from app.weather_service import get_weather
from app.crud import save_weather_data
from datetime import datetime

app = FastAPI()

Base.metadata.create_all(bind=engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/weather/collect")
def collect_weather(request: WeatherRequest, db: Session = Depends(get_db)):
    data = get_weather(
        request.latitude,
        request.longitude,
        request.start_date,
        request.end_date
    )
    times = data["hourly"]["time"]
    temperatures = data["hourly"]["temperature_2m"]
    
    
    save_weather_data(
        db,
        request.city,
        request.latitude,
        request.longitude,
        times,
        temperatures
    )
    return {
        "message": "Weather data saved successfully"
    }

@app.get("/weather/{city}")
def get_latest_weather(city: str, db:Session = Depends(get_db)):
    record = db.query(WeatherData).filter(WeatherData.city == city).order_by(WeatherData.timestamp.desc()).first()
    return record

@app.get("/weather/{city}/history")
def get_weather_history(city: str, start_date: str = Query(None), end_date: str = Query(None), db: Session = Depends(get_db)):
    query = db.query(WeatherData).filter(WeatherData.city == city)
    if start_date:
        query = query.filter(WeatherData.timestamp >= datetime.fromisoformat(start_date))
    if end_date:
        query = query.filter(WeatherData.timestamp <= datetime.fromisoformat(end_date))
    records = query.order_by(WeatherData.timestamp.desc()).all()
    return records

@app.get("/health")
def health():
    return {
        "status": "ok"
    }