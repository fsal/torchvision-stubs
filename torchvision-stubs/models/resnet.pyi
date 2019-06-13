# Stubs for torchvision.models.resnet (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import torch.nn as nn
from typing import Any, Optional

class BasicBlock(nn.Module):
    expansion: int = ...
    conv1: Any = ...
    bn1: Any = ...
    relu: Any = ...
    conv2: Any = ...
    bn2: Any = ...
    downsample: Any = ...
    stride: Any = ...
    def __init__(self, inplanes: Any, planes: Any, stride: int = ..., downsample: Optional[Any] = ..., groups: int = ..., base_width: int = ..., dilation: int = ..., norm_layer: Optional[Any] = ...) -> None: ...
    def forward(self, x: Any): ...

class Bottleneck(nn.Module):
    expansion: int = ...
    conv1: Any = ...
    bn1: Any = ...
    conv2: Any = ...
    bn2: Any = ...
    conv3: Any = ...
    bn3: Any = ...
    relu: Any = ...
    downsample: Any = ...
    stride: Any = ...
    def __init__(self, inplanes: Any, planes: Any, stride: int = ..., downsample: Optional[Any] = ..., groups: int = ..., base_width: int = ..., dilation: int = ..., norm_layer: Optional[Any] = ...) -> None: ...
    def forward(self, x: Any): ...

class ResNet(nn.Module):
    inplanes: int = ...
    dilation: int = ...
    groups: Any = ...
    base_width: Any = ...
    conv1: Any = ...
    bn1: Any = ...
    relu: Any = ...
    maxpool: Any = ...
    layer1: Any = ...
    layer2: Any = ...
    layer3: Any = ...
    layer4: Any = ...
    avgpool: Any = ...
    fc: Any = ...
    def __init__(self, block: Any, layers: Any, num_classes: int = ..., zero_init_residual: bool = ..., groups: int = ..., width_per_group: int = ..., replace_stride_with_dilation: Optional[Any] = ..., norm_layer: Optional[Any] = ...) -> None: ...
    def forward(self, x: Any): ...

def resnet18(pretrained: bool = ..., progress: bool = ..., **kwargs: Any): ...
def resnet34(pretrained: bool = ..., progress: bool = ..., **kwargs: Any): ...
def resnet50(pretrained: bool = ..., progress: bool = ..., **kwargs: Any): ...
def resnet101(pretrained: bool = ..., progress: bool = ..., **kwargs: Any): ...
def resnet152(pretrained: bool = ..., progress: bool = ..., **kwargs: Any): ...
def resnext50_32x4d(pretrained: bool = ..., progress: bool = ..., **kwargs: Any): ...
def resnext101_32x8d(pretrained: bool = ..., progress: bool = ..., **kwargs: Any): ...