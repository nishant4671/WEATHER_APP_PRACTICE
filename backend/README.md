# Weather App Backend

This is the backend API for the Weather App, built with FastAPI and deployed on Railway.app.

## Endpoints
- GET /api/weather/current/{city}
- GET /api/weather/forecast/{city}

## Local Development
1. Activate virtual environment: `venv\Scripts\activate`
2. Install dependencies: `pip install -r requirements.txt`
3. Run server: `uvicorn app.main:app --reload`

## Deployment
Deployed on Railway.app with automatic GitHub integration.
