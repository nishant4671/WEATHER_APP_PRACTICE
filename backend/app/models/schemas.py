from pydantic import BaseModel
from typing import List, Optional

class CurrentWeatherResponse(BaseModel):
    city: str
    temperature: float
    feels_like: float
    humidity: int
    pressure: int
    wind_speed: float
    description: str
    icon: str

class ForecastItem(BaseModel):
    datetime: str
    temperature: float
    feels_like: float
    humidity: int
    description: str
    icon: str

class ForecastResponse(BaseModel):
    city: str
    forecast: List[ForecastItem]

class ErrorResponse(BaseModel):
    error: str
    message: str