# -*- coding: utf-8 -*-

import asyncio
import httpx
import sys

async def test_weather():
    base = "http://localhost:8000"
    async with httpx.AsyncClient() as client:
        try:
            # Test current weather
            r = await client.get(f"{base}/api/weather/current/London", timeout=10)
            print(f"? Current London: {r.status_code}")
            if r.status_code == 200:
                data = r.json()
                print(f"   Temp: {data['temperature']} C")
            
            # Test forecast
            r = await client.get(f"{base}/api/weather/forecast/Paris", timeout=10)
            print(f"? Forecast Paris: {r.status_code}")
            if r.status_code == 200:
                data = r.json()
                print(f"   Forecasts: {len(data['forecast'])}")
                
        except Exception as e:
            print(f"? Test failed: {e}")
            return False
    return True

if __name__ == "__main__":
    success = asyncio.run(test_weather())
    sys.exit(0 if success else 1)
