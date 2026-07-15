from flask import Flask
from backend.routes import init_routes

app = Flask(__name__)

# Register all routes
init_routes(app)

if __name__ == "__main__":
    app.run(debug=True)