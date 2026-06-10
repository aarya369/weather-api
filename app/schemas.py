from pydantic import BaseModel
#Contains request validation.
class WeatherRequest(BaseModel):

    city: str

    latitude: float

    longitude: float

    start_date: str

    end_date: str

