#!/usr/bin/env python3
"""Simple test to verify .env is loading."""

import os
from dotenv import load_dotenv

# Load .env
load_dotenv()

print("🔍 Checking .env file...")
print(f"File exists: {os.path.exists('.env')}")

# Read raw file to check for BOM
with open('.env', 'rb') as f:
    raw = f.read(10)
    has_bom = raw.startswith(b'\xef\xbb\xbf')
    print(f"Has BOM (bad): {has_bom}")

# Check environment variables
print("\n📋 Environment Variables:")
keys = ['OPENWEATHER_API_KEY', 'DEBUG', 'PORT', 'CORS_ORIGINS']
for key in keys:
    value = os.getenv(key)
    if value:
        print(f"  ✅ {key}: {value[:15]}..." if len(value) > 15 else f"  ✅ {key}: {value}")
    else:
        print(f"  ❌ {key}: MISSING!")

# Test pydantic-settings
print("\n🔧 Testing pydantic-settings...")
try:
    from app.config import settings
    print("✅ Successfully loaded config!")
    print(f"   App: {settings.app_name}")
    print(f"   API Key (first 5): {settings.openweather_api_key[:5]}...")
    print(f"   Debug: {settings.debug}")
    print(f"   Port: {settings.port}")
    print(f"   CORS: {settings.cors_origins}")
except Exception as e:
    print(f"❌ Failed: {type(e).__name__}: {e}")
