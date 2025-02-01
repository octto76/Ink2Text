from transformers import TrOCRProcessor, VisionEncoderDecoderModel
import torch
import cv2

# Load model
processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")
model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten")

def recognize_handwriting(image):
    image = cv2.resize(image, (384, 384))  # Resize for model input
    image = image / 255.0  # Normalize
    pixel_values = processor(images=image, return_tensors="pt").pixel_values

    with torch.no_grad():
        generated_ids = model.generate(pixel_values)
        text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

    return text
