# Stubs for torchvision.models._utils (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from torch import nn
from typing import Any

class IntermediateLayerGetter(nn.ModuleDict):
    return_layers: Any = ...
    def __init__(self, model: Any, return_layers: Any) -> None: ...
    def forward(self, x: Any): ...
