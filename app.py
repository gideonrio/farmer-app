import sys
import os

# FIX: Prevent Groq/Httpx from crashing due to unexpected proxy configuration
os.environ.pop('HTTP_PROXY', None)
os.environ.pop('HTTPS_PROXY', None)
os.environ.pop('http_proxy', None)
os.environ.pop('https_proxy', None)

# Provide an absolute path reference to prevent module loading issues
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Smart-AI-Farm')
sys.path.insert(0, BASE_DIR)

from backend.app import create_app

if __name__ == '__main__':
    try:
        import traceback
        app = create_app()
        import socket
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        print("\n" + "="*50)
        print("          SMART AI FARM - SERVER ACTIVE")
        print("="*50)
        print(f"Network Access: http://{local_ip}:5000")
        print("="*50 + "\n")
        app.run(debug=False, host='0.0.0.0', port=5000)
    except Exception as e:
        print(f"CRITICAL ERROR: {e}")
        traceback.print_exc()
