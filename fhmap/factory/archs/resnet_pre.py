from typing import Callable, List, Type

import os
import torch
import torch.nn as nn
from torchvision import models
from fhmap.factory.imagenet100_classes import imagenet100_ids

device = "cuda" if torch.cuda.is_available() else "cpu"

class ResnetImagenet100(nn.Module):
    """
    Resnet class for the imagenet100 dataset. Uses a pretrained resnet
    and only gets the predictions of the ids of the imagenet100 objects
    """
    def __init__(self,pretrained,num_classes):
        super().__init__()
        self.model = models.resnet50(pretrained=True)
        self.ids = torch.tensor(imagenet100_ids,dtype=torch.long)
        self.model.eval()
    def forward(self, image: torch.Tensor) -> torch.Tensor:
        out = self.model(image) # get resnet output
        out = out[:,self.ids]   # filter imagenet100 classes
        return out