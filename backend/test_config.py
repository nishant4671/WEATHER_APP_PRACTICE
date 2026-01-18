#!/usr/bin/env python3
"""Test script to verify environment configuration is working."""

import sys
sys.path.insert(0, '.')

try:
    from app.config import settings
    
    print("=" * 50)
    print("? CONFIGURATION TEST SUCCESSFUL!")
    print("=" * 50)
    
    print(f"\n?? APP INFORMATION:")
    print(f"   Name: {settings.app_name}")
    print(f"   Version: {settings.version}")
    
    print(f"\n?? API CONFIGURATION:")
    print(f"   OpenWeatherMap Key: {settings.openweather_api_key[:10]}...")
    print(f"   Base URL: {settings.openweather_base_url}")
    
    print(f"\n?? CORS CONFIGURATION:")
    print(f"   Origins: {settings.cors_origins}")
    
    print(f"\n??  SERVER CONFIGURATION:")
    print(f"   Host: {settings.host}")
    print(f"   Port: {settings.port}")
    print(f"   Debug: {settings.debug}")
    
    print(f"\n?? ENVIRONMENT:")
    print(f"   Environment file: .env")
    
    # Security check
    if "your_key" in settings.openweather_api_key.lower():
        print(f"\n??  WARNING: Using placeholder API key!")
    else:
        print(f"\n? Security: Real API key detected!")
        
    print(f"\n" + "=" * 50)
    print("?? CONFIGURATION READY FOR FASTAPI DEVELOPMENT!")
    print("=" * 50)
    
except Exception as e:
    print(f"\n? ERROR LOADING CONFIGURATION:")
    print(f"   {type(e).__name__}: {e}")
    print(f"\n?? TROUBLESHOOTING:")
    print(f"   1. Check .env file exists and has correct format")
    print(f"   2. Make sure OPENWEATHER_API_KEY has a real value")
    print(f"   3. Ensure pydantic-settings is installed: pip install pydantic-settings")
    print(f"   4. Check for typos in environment variable names")
    sys.exit(1)
