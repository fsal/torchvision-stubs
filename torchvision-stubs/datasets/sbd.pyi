# Stubs for torchvision.datasets.sbd (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .utils import download_url
from .vision import VisionDataset
from .voc import download_extract
from typing import Any, Optional

class SBDataset(VisionDataset):
    url: str = ...
    md5: str = ...
    filename: str = ...
    voc_train_url: str = ...
    voc_split_filename: str = ...
    voc_split_md5: str = ...
    image_set: Any = ...
    mode: Any = ...
    num_classes: int = ...
    images: Any = ...
    masks: Any = ...
    def __init__(self, root: Any, image_set: str = ..., mode: str = ..., download: bool = ..., transforms: Optional[Any] = ...) -> None: ...
    def __getitem__(self, index: Any): ...
    def __len__(self): ...
    def extra_repr(self): ...