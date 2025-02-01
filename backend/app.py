from flask import Flask
from routes import ocr_routes
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend

# Register routes
app.register_blueprint(ocr_routes)

if __name__ == "__main__":
    app.run(debug=True)
