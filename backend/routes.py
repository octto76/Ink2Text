from flask import Blueprint, request, jsonify
import cv2
import numpy as np
from models.ocr_model import recognize_handwriting

ocr_routes = Blueprint('ocr_routes', __name__)

@ocr_routes.route("/upload", methods=["POST"])
def upload_image():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    image = np.frombuffer(file.read(), np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)

    # Process image with OCR model
    recognized_text = recognize_handwriting(image)

    return jsonify({"latex": recognized_text})
