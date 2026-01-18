#!/usr/bin/env python3
"""
Simple script to run the FastAPI application.
Use this for local development.
"""

import uvicorn
from app.config import settings

if __name__ == "__main__":
    print("🚀 Starting Weather App Backend...")
    print(f"📱 App: {settings.app_name} v{settings.version}")
    print(f"🌐 Host: {settings.host}")
    print(f"🚪 Port: {settings.port}")
    print(f"🐛 Debug: {settings.debug}")
    print(f"🔑 API Key configured: {'Yes' if settings.openweather_api_key else 'No'}")
    print("\n📚 Available endpoints:")
    print("   • http://localhost:8000/           - Welcome")
    print("   • http://localhost:8000/health     - Health check")
    print("   • http://localhost:8000/info       - App info")
    print("   • http://localhost:8000/docs       - Swagger UI")
    print("   • http://localhost:8000/redoc      - ReDoc")
    print("\n🛑 Press Ctrl+C to stop the server")
    print("=" * 50)
    
    # Run the server
    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,  # Auto-reload on code changes
        log_level="info"
    )
