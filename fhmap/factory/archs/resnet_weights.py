import torch
import torch.nn as nn
from torchvision import models

device = "cuda" if torch.cuda.is_available() else "cpu"

class ResnetWeight(nn.Module):
    """
    Resnet class that loads weights given by a filepath
    """
    def __init__(self,pretrained,num_classes):
        super().__init__()
    def load_state_dict(self,filepath):
        self.model = models.resnet50(pretrained=False)
        d = self.model.fc.in_features
        self.model.fc = nn.Linear(d, 2)
        self.model.eval()
        weights = torch.load(filepath)
        self.model.load_state_dict(weights)
    def forward(self, image: torch.Tensor) -> torch.Tensor:
        return self.model(image) 
