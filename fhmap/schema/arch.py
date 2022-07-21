from abc import ABC
from dataclasses import dataclass

from omegaconf import MISSING


@dataclass
class ArchConfig(ABC):
    _target_: str = MISSING


@dataclass
class Resnet50Config(ArchConfig):
    _target_: str = "torchvision.models.resnet50"
    pretrained: bool = False


@dataclass
class Resnet56Config(ArchConfig):
    _target_: str = "fhmap.factory.archs.resnet.resnet56"
    pretrained: bool = False


@dataclass
class Wideresnet40Config(ArchConfig):
    _target_: str = "fhmap.factory.archs.wideresnet.wideresnet40"
    widening_factor: int = MISSING
    droprate: float = MISSING

@dataclass
class CLIPConfig(ArchConfig):
    _target_: str = "fhmap.factory.archs.clip.CLIP"

@dataclass
class ResnetImagenet100Config(ArchConfig):
    _target_: str = "fhmap.factory.archs.resnet_pre.ResnetImagenet100"

@dataclass
class ResnetWeights2(ArchConfig):
    _target_: str = "fhmap.factory.archs.resnet_weights.ResnetWeight"
@dataclass
class DFRConfig(ArchConfig):
    _target_: str = "fhmap.factory.archs.dfr.DFR"

# NOTE: If you want to add your architecture, please implement YourCustomArchConfig class here.
