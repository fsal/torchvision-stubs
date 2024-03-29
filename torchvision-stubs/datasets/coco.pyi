# Stubs for torchvision.datasets.coco (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .vision import VisionDataset
from typing import Any, Optional

class CocoCaptions(VisionDataset):
    coco: Any = ...
    ids: Any = ...
    def __init__(self, root: Any, annFile: Any, transform: Optional[Any] = ..., target_transform: Optional[Any] = ..., transforms: Optional[Any] = ...) -> None: ...
    def __getitem__(self, index: Any): ...
    def __len__(self): ...

class CocoDetection(VisionDataset):
    coco: Any = ...
    ids: Any = ...
    def __init__(self, root: Any, annFile: Any, transform: Optional[Any] = ..., target_transform: Optional[Any] = ..., transforms: Optional[Any] = ...) -> None: ...
    def __getitem__(self, index: Any): ...
    def __len__(self): ...
