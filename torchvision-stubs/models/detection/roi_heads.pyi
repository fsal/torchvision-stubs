# Stubs for torchvision.models.detection.roi_heads (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import torch.nn.functional
from typing import Any, Optional

def fastrcnn_loss(class_logits: Any, box_regression: Any, labels: Any, regression_targets: Any): ...
def maskrcnn_inference(x: Any, labels: Any): ...
def project_masks_on_boxes(gt_masks: Any, boxes: Any, matched_idxs: Any, M: Any): ...
def maskrcnn_loss(mask_logits: Any, proposals: Any, gt_masks: Any, gt_labels: Any, mask_matched_idxs: Any): ...
def keypoints_to_heatmap(keypoints: Any, rois: Any, heatmap_size: Any): ...
def heatmaps_to_keypoints(maps: Any, rois: Any): ...
def keypointrcnn_loss(keypoint_logits: Any, proposals: Any, gt_keypoints: Any, keypoint_matched_idxs: Any): ...
def keypointrcnn_inference(x: Any, boxes: Any): ...
def expand_boxes(boxes: Any, scale: Any): ...
def expand_masks(mask: Any, padding: Any): ...
def paste_mask_in_image(mask: Any, box: Any, im_h: Any, im_w: Any): ...
def paste_masks_in_image(masks: Any, boxes: Any, img_shape: Any, padding: int = ...): ...

class RoIHeads(torch.nn.Module):
    box_similarity: Any = ...
    proposal_matcher: Any = ...
    fg_bg_sampler: Any = ...
    box_coder: Any = ...
    box_roi_pool: Any = ...
    box_head: Any = ...
    box_predictor: Any = ...
    score_thresh: Any = ...
    nms_thresh: Any = ...
    detections_per_img: Any = ...
    mask_roi_pool: Any = ...
    mask_head: Any = ...
    mask_predictor: Any = ...
    keypoint_roi_pool: Any = ...
    keypoint_head: Any = ...
    keypoint_predictor: Any = ...
    def __init__(self, box_roi_pool: Any, box_head: Any, box_predictor: Any, fg_iou_thresh: Any, bg_iou_thresh: Any, batch_size_per_image: Any, positive_fraction: Any, bbox_reg_weights: Any, score_thresh: Any, nms_thresh: Any, detections_per_img: Any, mask_roi_pool: Optional[Any] = ..., mask_head: Optional[Any] = ..., mask_predictor: Optional[Any] = ..., keypoint_roi_pool: Optional[Any] = ..., keypoint_head: Optional[Any] = ..., keypoint_predictor: Optional[Any] = ...) -> None: ...
    @property
    def has_mask(self): ...
    @property
    def has_keypoint(self): ...
    def assign_targets_to_proposals(self, proposals: Any, gt_boxes: Any, gt_labels: Any): ...
    def subsample(self, labels: Any): ...
    def add_gt_proposals(self, proposals: Any, gt_boxes: Any): ...
    def check_targets(self, targets: Any) -> None: ...
    def select_training_samples(self, proposals: Any, targets: Any): ...
    def postprocess_detections(self, class_logits: Any, box_regression: Any, proposals: Any, image_shapes: Any): ...
    def forward(self, features: Any, proposals: Any, image_shapes: Any, targets: Optional[Any] = ...): ...
