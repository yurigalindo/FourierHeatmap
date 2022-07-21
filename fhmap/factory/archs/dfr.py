import torch.nn as nn
import pickle
import torch
from torchvision import models

class DFR(nn.Module):
    def __init__(self,pretrained,num_classes):
        super().__init__()
    def load_state_dict(self,filepath):
        self._load_embedding(filepath / "resnet.pt")
        self._load_logistic_regression(filepath / "logreg.pkl")
        self._load_scaler(filepath / "scaler.pkl")
    def get_embedding(self,image: torch.Tensor):
        x = self.embedding.conv1(image)
        x = self.embedding.bn1(x)
        x = self.embedding.relu(x)
        x = self.embedding.maxpool(x)

        x = self.embedding.layer1(x)
        x = self.embedding.layer2(x)
        x = self.embedding.layer3(x)
        x = self.embedding.layer4(x)

        x = self.embedding.avgpool(x)
        x = torch.flatten(x, 1)
        return x

    def forward(self, image: torch.Tensor) -> torch.Tensor:
        embeddings = self.get_embedding(image.cuda()).detach().cpu().numpy()
        transformed = self.scaler.transform(embeddings)
        prediction = self.logreg.predict_proba(transformed)
        return torch.from_numpy(prediction).to("cuda:0")
    def _load_embedding(self,filepath):
        self.embedding = models.resnet50(pretrained=False)
        d = self.embedding.fc.in_features
        self.embedding.fc = nn.Linear(d, 2)
        self.embedding.eval()
        weights = torch.load(filepath) #load the weights
        self.embedding.load_state_dict(weights)
    def _load_logistic_regression(self,filepath):
        self.logreg = pickle.load(open(filepath,"rb"))
    def _load_scaler(self,filepath):
        self.scaler = pickle.load(open(filepath,"rb"))