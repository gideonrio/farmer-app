import os
import sys

# Add the Smart-AI-Farm directory to the path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.join(BASE_DIR, 'Smart-AI-Farm')
if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)

from backend.app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
