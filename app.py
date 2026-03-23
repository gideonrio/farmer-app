import sys
import os
from flask import Flask, jsonify

# FIX: Prevent proxy conflicts
os.environ.pop('HTTP_PROXY', None)
os.environ.pop('HTTPS_PROXY', None)
os.environ.pop('http_proxy', None)
os.environ.pop('https_proxy', None)

# Optional: add Smart-AI-Farm path if exists
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Smart-AI-Farm')
if os.path.exists(BASE_DIR):
    sys.path.insert(0, BASE_DIR)

# Create Flask app directly
app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "running",
        "app": "Smart AI Farm",
        "message": "App deployed successfully on Render 🚀"
    })

@app.route("/health")
def health():
    return "OK", 200


if __name__ == '__main__':
    try:
        import socket
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)

        print("\n" + "="*50)
        print(" SMART AI FARM - SERVER ACTIVE ")
        print("="*50)
        print(f"Network Access: http://{local_ip}:5000")
        print("="*50 + "\n")

        app.run(host="0.0.0.0", port=5000)

    except Exception as e:
        import traceback
        print(f"CRITICAL ERROR: {e}")
        traceback.print_exc()
