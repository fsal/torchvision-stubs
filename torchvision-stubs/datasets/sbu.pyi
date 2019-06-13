# Stubs for torchvision.datasets.sbu (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .utils import check_integrity, download_url
from .vision import VisionDataset
from typing import Any, Optional

class SBU(VisionDataset):
    url: str = ...
    filename: str = ...
    md5_checksum: str = ...
    transform: Any = ...
    target_transform: Any = ...
    photos: Any = ...
    captions: Any = ...
    def __init__(self, root: Any, transform: Optional[Any] = ..., target_transform: Optional[Any] = ..., download: bool = ...) -> None: ...
    def __getitem__(self, index: Any): ...
    def __len__(self): ...
    def download(self) -> None: ...
