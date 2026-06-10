from app.weather_service import get_weather

data = get_weather(
    19.07,
    72.87,
    "2026-05-08",
    "2026-05-09"
)

times = data["hourly"]["time"] 
temps = data["hourly"]["temperature_2m"]

for t, temp in zip(times, temps):
    print(f"{t} \t {temp}")