# Stubs for torchvision.models.segmentation._utils (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from torch import nn
from typing import Any, Optional

class _SimpleSegmentationModel(nn.Module):
    backbone: Any = ...
    classifier: Any = ...
    aux_classifier: Any = ...
    def __init__(self, backbone: Any, classifier: Any, aux_classifier: Optional[Any] = ...) -> None: ...
    def forward(self, x: Any): ...
