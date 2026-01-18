#!/usr/bin/env python3
"""
Test script to verify FastAPI endpoints are working.
"""

import requests
import time
import sys

BASE_URL = "http://localhost:8000"
ENDPOINTS = [
    "/",
    "/health", 
    "/info",
    "/docs",
    "/redoc"
]

def test_endpoints():
    print("🔍 Testing FastAPI Endpoints...")
    print("=" * 50)
    
    for endpoint in ENDPOINTS:
        url = BASE_URL + endpoint
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"✅ {endpoint:20} - Status: {response.status_code}")
                if endpoint == "/health":
                    data = response.json()
                    print(f"   Status: {data.get('status', 'unknown')}")
            else:
                print(f"⚠️  {endpoint:20} - Status: {response.status_code}")
        except requests.exceptions.ConnectionError:
            print(f"❌ {endpoint:20} - Cannot connect (is server running?)")
            print(f"   Run: python run.py")
            return False
        except Exception as e:
            print(f"❌ {endpoint:20} - Error: {type(e).__name__}: {e}")
    
    print("=" * 50)
    print("📊 Summary:")
    print("   • Server should be running on http://localhost:8000")
    print("   • Open http://localhost:8000/docs for Swagger UI")
    print("   • Health endpoint is CRITICAL for Railway deployment")
    return True

if __name__ == "__main__":
    # Wait a moment for server to start if just started
    time.sleep(1)
    success = test_endpoints()
    sys.exit(0 if success else 1)
