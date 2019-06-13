# Stubs for torchvision.models.detection._utils (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import torch
from typing import Any

class BalancedPositiveNegativeSampler:
    batch_size_per_image: Any = ...
    positive_fraction: Any = ...
    def __init__(self, batch_size_per_image: Any, positive_fraction: Any) -> None: ...
    def __call__(self, matched_idxs: Any): ...

def encode_boxes(reference_boxes: torch.Tensor, proposals: torch.Tensor, weights: torch.Tensor) -> torch.Tensor: ...

class BoxCoder:
    weights: Any = ...
    bbox_xform_clip: Any = ...
    def __init__(self, weights: Any, bbox_xform_clip: Any = ...) -> None: ...
    def encode(self, reference_boxes: Any, proposals: Any): ...
    def encode_single(self, reference_boxes: Any, proposals: Any): ...
    def decode(self, rel_codes: Any, boxes: Any): ...
    def decode_single(self, rel_codes: Any, boxes: Any): ...

class Matcher:
    BELOW_LOW_THRESHOLD: int = ...
    BETWEEN_THRESHOLDS: int = ...
    high_threshold: Any = ...
    low_threshold: Any = ...
    allow_low_quality_matches: Any = ...
    def __init__(self, high_threshold: Any, low_threshold: Any, allow_low_quality_matches: bool = ...) -> None: ...
    def __call__(self, match_quality_matrix: Any): ...
    def set_low_quality_matches_(self, matches: Any, all_matches: Any, match_quality_matrix: Any) -> None: ...