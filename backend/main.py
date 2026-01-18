"""
Main FastAPI application file.
This is the entry point for the Weather App backend.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings


# Create FastAPI application instance
app = FastAPI(
    title=settings.app_name,
    description="Weather App Backend API",
    version=settings.version,
    docs_url="/docs",  # Enable Swagger UI at /docs
    redoc_url="/redoc",  # Enable ReDoc at /redoc
)

# Configure CORS (Cross-Origin Resource Sharing)
# CRITICAL: Allows frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Import routers (API endpoints) - we'll create these later
# from app.api import weather

# Include routers
# app.include_router(weather.router, prefix="/api/weather", tags=["weather"])


# ============ BASIC ENDPOINTS ============

@app.get("/")
async def root():
    """Root endpoint - welcome message."""
    return {
        "message": f"Welcome to {settings.app_name}!",
        "version": settings.version,
        "status": "running",
        "docs": "/docs",
        "health": "/health"
    }


@app.get("/health")
async def health_check():
    """
    Health check endpoint.
    CRITICAL FOR RAILWAY: Railway.app monitors this endpoint.
    """
    return {
        "status": "healthy",
        "service": settings.app_name,
        "version": settings.version,
        "environment": "development"
    }


@app.get("/info")
async def app_info():
    """Get application information and configuration."""
    return {
        "app": settings.app_name,
        "version": settings.version,
        "debug": settings.debug,
        "cors_enabled": True,
        "cors_origins": settings.cors_origins,
        "api_base_url": settings.openweather_base_url,
        "api_key_configured": bool(settings.openweather_api_key),
    }


# ============ ERROR HANDLERS ============

@app.get("/test/error")
async def test_error():
    """Test endpoint to simulate an error (for development)."""
    raise ValueError("This is a test error to check error handling")


# Development note: We'll add more endpoints in Step 7
print(f"✅ {settings.app_name} v{settings.version} initialized!")
print(f"🌐 API Base URL: {settings.openweather_base_url}")
print(f"🔑 API Key configured: {'Yes' if settings.openweather_api_key else 'No'}")
print(f"🚀 Server will run on: http://{settings.host}:{settings.port}")
print(f"📚 API Documentation: http://{settings.host}:{settings.port}/docs")