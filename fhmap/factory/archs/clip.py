from typing import Callable, List, Type

import os
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.nn.init as init
from torchvision.datasets import CIFAR10
import clip
from fhmap.factory.imagenet100_classes import imagenet100_classes


device = "cuda" if torch.cuda.is_available() else "cpu"
cifar10 = CIFAR10(root=os.path.expanduser("~/.cache"), download=True, train=False)

class CLIP(nn.Module):
    def __init__(self,pretrained,num_classes):
        super(CLIP, self).__init__()
        self.clip, self.preprocess = clip.load('ViT-B/32', device)
        #self.text_inputs = torch.cat([clip.tokenize(f"a photo of a {c}") for c in cifar10.classes]).to(device)
        self.text_inputs = torch.cat([clip.tokenize(f"a photo of a {c}") for c in imagenet100_classes]).to(device)
    def forward(self, image: torch.Tensor) -> torch.Tensor:
        return self.clip(self.preprocess(image).to(device),self.text_inputs)[0]