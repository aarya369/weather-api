import requests
def get_weather(latitude, longitude, start_date, end_date):
    url = ("https://archive-api.open-meteo.com/v1/archive")
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": start_date,
        "end_date": end_date,
        "hourly": "temperature_2m",
        "timezone": "Asia/Kolkata"
    }
    response = requests.get(url, params = params)
    return response.json()
    