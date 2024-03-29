# Stubs for torchvision.ops.poolers (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from torch import nn
from typing import Any

class LevelMapper:
    k_min: Any = ...
    k_max: Any = ...
    s0: Any = ...
    lvl0: Any = ...
    eps: Any = ...
    def __init__(self, k_min: Any, k_max: Any, canonical_scale: int = ..., canonical_level: int = ..., eps: float = ...) -> None: ...
    def __call__(self, boxlists: Any): ...

class MultiScaleRoIAlign(nn.Module):
    featmap_names: Any = ...
    sampling_ratio: Any = ...
    output_size: Any = ...
    scales: Any = ...
    map_levels: Any = ...
    def __init__(self, featmap_names: Any, output_size: Any, sampling_ratio: Any) -> None: ...
    def convert_to_roi_format(self, boxes: Any): ...
    def infer_scale(self, feature: Any, original_size: Any): ...
    def setup_scales(self, features: Any, image_shapes: Any) -> None: ...
    def forward(self, x: Any, boxes: Any, image_shapes: Any): ...
