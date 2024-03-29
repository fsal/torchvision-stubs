# Stubs for torchvision.datasets.imagenet (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .folder import ImageFolder
from .utils import check_integrity, download_url
from typing import Any, Optional

ARCHIVE_DICT: Any

class ImageNet(ImageFolder):
    split: Any = ...
    root: Any = ...
    wnids: Any = ...
    wnid_to_idx: Any = ...
    classes: Any = ...
    class_to_idx: Any = ...
    def __init__(self, root: Any, split: str = ..., download: bool = ..., **kwargs: Any) -> None: ...
    def download(self) -> None: ...
    @property
    def meta_file(self): ...
    @property
    def valid_splits(self): ...
    @property
    def split_folder(self): ...
    def extra_repr(self): ...

def extract_tar(src: Any, dest: Optional[Any] = ..., gzip: Optional[Any] = ..., delete: bool = ...) -> None: ...
def download_and_extract_tar(url: Any, download_root: Any, extract_root: Optional[Any] = ..., filename: Optional[Any] = ..., md5: Optional[Any] = ..., **kwargs: Any) -> None: ...
def parse_devkit(root: Any): ...
def parse_meta(devkit_root: Any, path: str = ..., filename: str = ...): ...
def parse_val_groundtruth(devkit_root: Any, path: str = ..., filename: str = ...): ...
def prepare_train_folder(folder: Any) -> None: ...
def prepare_val_folder(folder: Any, wnids: Any) -> None: ...
