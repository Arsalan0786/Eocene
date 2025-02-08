import torch
import torch.nn as nn
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image
import sys

# Load Pre-trained MobileNetV2 Model
model = models.mobilenet_v2(pretrained=True)

# Modify the Last Layer for 4 Classes
num_features = model.classifier[1].in_features
model.classifier[1] = nn.Linear(num_features, 4)  # 4 Categories: Plastic, Paper, Organic, Electronic

# Load Trained Model (If Available)
try:
    model.load_state_dict(torch.load("waste_model.pth", map_location=torch.device('cpu')))
    print("Loaded trained model successfully!")
except:
    print("No trained model found. Using default pre-trained model.")

model.eval()  # Set model to evaluation mode

# Define Class Labels
class_labels = ["Plastic", "Paper", "Organic", "Electronic"]

# Define Image Transformations (Resize, Convert to Tensor, Normalize)
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

# Function to Predict Waste Category
def predict_image(image_path):
    try:
        image = Image.open(image_path).convert("RGB")
        image = transform(image).unsqueeze(0)  # Add batch dimension

        with torch.no_grad():
            outputs = model(image)
            _, predicted = torch.max(outputs, 1)

        return class_labels[predicted.item()]
    
    except Exception as e:
        return f"Error: {e}"

# Run Directly From Terminal (If File is Run)
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python waste_classifier.py <image_path>")
    else:
        image_path = sys.argv[1]
        result = predict_image(image_path)
        print(f"Predicted Waste Category: {result}")
