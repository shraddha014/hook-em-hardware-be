# main.py
import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))  # Use PORT from environment variables or default to 5000
    app.run(host="0.0.0.0", port=port, debug=True)
