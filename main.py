from fastapi import FastAPI, File, UploadFile
from PIL import Image
import tensorflow as tf
import io

# Load pre-trained AI model (MobileNetV2 for waste classification)
model = tf.keras.applications.MobileNetV2(weights="imagenet")

# Initialize FastAPI app
app = FastAPI()

# Class labels (replace with your trained model's labels if available)
LABELS = {0: "Plastic", 1: "Paper", 2: "Organic", 3: "Electronic"}

# Image preprocessing function
def preprocess_image(image):
    image = image.resize((224, 224))  # Resize for model input
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = tf.keras.applications.mobilenet_v2.preprocess_input(image)
    return tf.expand_dims(image, axis=0)  # Add batch dimension

@app.post("/predict/")
async def predict_waste(file: UploadFile = File(...)):
    # Read image
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")

    # Preprocess image & make prediction
    input_tensor = preprocess_image(image)
    predictions = model.predict(input_tensor)
    predicted_class = tf.argmax(predictions[0]).numpy()

    # Return prediction result
    return {"category": LABELS.get(predicted_class, "Unknown")}

# Run the server (if running locally)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
