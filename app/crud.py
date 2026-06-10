from datetime import datetime
from app.models import WeatherData
def save_weather_data(db, city, latitude, longitude, times, temperatures):
    for t, temp in zip(times, temperatures):
        record = WeatherData(
            city=city,
            latitude=latitude,
            longitude=longitude,
            timestamp=datetime.fromisoformat(t),
            temperature=temp,
            created_at=datetime.utcnow()
        )
        db.add(record)
    db.commit()