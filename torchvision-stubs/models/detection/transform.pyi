# Stubs for torchvision.models.detection.transform (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .image_list import ImageList
from .roi_heads import paste_masks_in_image
from torch import nn
from typing import Any, Optional

class GeneralizedRCNNTransform(nn.Module):
    min_size: Any = ...
    max_size: Any = ...
    image_mean: Any = ...
    image_std: Any = ...
    def __init__(self, min_size: Any, max_size: Any, image_mean: Any, image_std: Any) -> None: ...
    def forward(self, images: Any, targets: Optional[Any] = ...): ...
    def normalize(self, image: Any): ...
    def resize(self, image: Any, target: Any): ...
    def batch_images(self, images: Any, size_divisible: int = ...): ...
    def postprocess(self, result: Any, image_shapes: Any, original_image_sizes: Any): ...

def resize_keypoints(keypoints: Any, original_size: Any, new_size: Any): ...
def resize_boxes(boxes: Any, original_size: Any, new_size: Any): ...
