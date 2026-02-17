from flask import Flask
import os
app = Flask(__name__)

BACKEND_NAME = os.environ.get("BACKEND_NAME", "backend?")

@app.route("/")
def index():
    return f"Served by backend: {BACKEND_NAME}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
