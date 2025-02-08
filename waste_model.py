import torch
import torchvision.models as models
from torchvision.models import MobileNet_V2_Weights

# Load Pre-trained MobileNetV2 Model Using Correct Syntax
model = models.mobilenet_v2(weights=MobileNet_V2_Weights.IMAGENET1K_V1)

# Modify the Final Layer for 4 Classes
num_features = model.classifier[1].in_features
model.classifier[1] = torch.nn.Linear(num_features, 4)

# Save the Model
torch.save(model.state_dict(), "waste_model.pth")

print("Model saved successfully without warnings!")
