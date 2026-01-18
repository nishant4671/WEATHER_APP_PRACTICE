import httpx
from app.config import settings
import asyncio

class WeatherService:
    def __init__(self):
        self.api_key = settings.openweather_api_key
        self.base_url = settings.openweather_base_url
        self.client = httpx.AsyncClient(timeout=30.0)
    
    async def get_current_weather(self, city: str):
        url = f"{self.base_url}/weather"
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }
        response = await self.client.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    async def get_forecast(self, city: str):
        url = f"{self.base_url}/forecast"
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }
        response = await self.client.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    async def close(self):
        await self.client.aclose()

weather_service = WeatherService()