# Stubs for torchvision.models.squeezenet (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import torch.nn.init as nn
from typing import Any

class Fire(nn.Module):
    inplanes: Any = ...
    squeeze: Any = ...
    squeeze_activation: Any = ...
    expand1x1: Any = ...
    expand1x1_activation: Any = ...
    expand3x3: Any = ...
    expand3x3_activation: Any = ...
    def __init__(self, inplanes: Any, squeeze_planes: Any, expand1x1_planes: Any, expand3x3_planes: Any) -> None: ...
    def forward(self, x: Any): ...

class SqueezeNet(nn.Module):
    num_classes: Any = ...
    features: Any = ...
    classifier: Any = ...
    def __init__(self, version: str = ..., num_classes: int = ...) -> None: ...
    def forward(self, x: Any): ...

def squeezenet1_0(pretrained: bool = ..., progress: bool = ..., **kwargs: Any): ...
def squeezenet1_1(pretrained: bool = ..., progress: bool = ..., **kwargs: Any): ...