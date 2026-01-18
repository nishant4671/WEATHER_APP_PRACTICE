from fastapi import APIRouter, HTTPException
from app.services.weather_service import weather_service
from app.models.schemas import CurrentWeatherResponse, ForecastResponse, ErrorResponse
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/current/{city}", response_model=CurrentWeatherResponse)
async def get_current_weather(city: str):
    try:
        data = await weather_service.get_current_weather(city)
        
        return CurrentWeatherResponse(
            city=data["name"],
            temperature=data["main"]["temp"],
            feels_like=data["main"]["feels_like"],
            humidity=data["main"]["humidity"],
            pressure=data["main"]["pressure"],
            wind_speed=data["wind"]["speed"],
            description=data["weather"][0]["description"],
            icon=data["weather"][0]["icon"]
        )
    except Exception as e:
        logger.error(f"Weather API error for {city}: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/forecast/{city}", response_model=ForecastResponse)
async def get_forecast(city: str):
    try:
        data = await weather_service.get_forecast(city)
        
        forecast_items = []
        for item in data["list"][:5]:  # First 5 forecasts
            forecast_items.append({
                "datetime": item["dt_txt"],
                "temperature": item["main"]["temp"],
                "feels_like": item["main"]["feels_like"],
                "humidity": item["main"]["humidity"],
                "description": item["weather"][0]["description"],
                "icon": item["weather"][0]["icon"]
            })
        
        return ForecastResponse(
            city=data["city"]["name"],
            forecast=forecast_items
        )
    except Exception as e:
        logger.error(f"Forecast API error for {city}: {e}")
        raise HTTPException(status_code=500, detail=str(e))