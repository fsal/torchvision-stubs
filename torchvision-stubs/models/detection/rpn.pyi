# Stubs for torchvision.models.detection.rpn (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import torch
from torch import nn
from typing import Any, Optional

class AnchorGenerator(nn.Module):
    sizes: Any = ...
    aspect_ratios: Any = ...
    cell_anchors: Any = ...
    def __init__(self, sizes: Any = ..., aspect_ratios: Any = ...) -> None: ...
    @staticmethod
    def generate_anchors(scales: Any, aspect_ratios: Any, device: str = ...): ...
    def set_cell_anchors(self, device: Any): ...
    def num_anchors_per_location(self): ...
    def grid_anchors(self, grid_sizes: Any, strides: Any): ...
    def cached_grid_anchors(self, grid_sizes: Any, strides: Any): ...
    def forward(self, image_list: Any, feature_maps: Any): ...

class RPNHead(nn.Module):
    conv: Any = ...
    cls_logits: Any = ...
    bbox_pred: Any = ...
    def __init__(self, in_channels: Any, num_anchors: Any) -> None: ...
    def forward(self, x: Any): ...

def permute_and_flatten(layer: Any, N: Any, A: Any, C: Any, H: Any, W: Any): ...
def concat_box_prediction_layers(box_cls: Any, box_regression: Any): ...

class RegionProposalNetwork(torch.nn.Module):
    anchor_generator: Any = ...
    head: Any = ...
    box_coder: Any = ...
    box_similarity: Any = ...
    proposal_matcher: Any = ...
    fg_bg_sampler: Any = ...
    nms_thresh: Any = ...
    min_size: int = ...
    def __init__(self, anchor_generator: Any, head: Any, fg_iou_thresh: Any, bg_iou_thresh: Any, batch_size_per_image: Any, positive_fraction: Any, pre_nms_top_n: Any, post_nms_top_n: Any, nms_thresh: Any) -> None: ...
    @property
    def pre_nms_top_n(self): ...
    @property
    def post_nms_top_n(self): ...
    def assign_targets_to_anchors(self, anchors: Any, targets: Any): ...
    def filter_proposals(self, proposals: Any, objectness: Any, image_shapes: Any, num_anchors_per_level: Any): ...
    def compute_loss(self, objectness: Any, pred_bbox_deltas: Any, labels: Any, regression_targets: Any): ...
    def forward(self, images: Any, features: Any, targets: Optional[Any] = ...): ...