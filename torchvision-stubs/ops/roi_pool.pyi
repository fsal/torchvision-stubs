# Stubs for torchvision.ops.roi_pool (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ._utils import convert_boxes_to_roi_format
from torch import nn
from torch.autograd import Function
from typing import Any

class _RoIPoolFunction(Function):
    @staticmethod
    def forward(ctx: Any, input: Any, rois: Any, output_size: Any, spatial_scale: Any): ...
    @staticmethod
    def backward(ctx: Any, grad_output: Any): ...

def roi_pool(input: Any, boxes: Any, output_size: Any, spatial_scale: float = ...): ...

class RoIPool(nn.Module):
    output_size: Any = ...
    spatial_scale: Any = ...
    def __init__(self, output_size: Any, spatial_scale: Any) -> None: ...
    def forward(self, input: Any, rois: Any): ...
