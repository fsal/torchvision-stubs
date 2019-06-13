# Stubs for torchvision.datasets.mnist (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .utils import download_url, makedir_exist_ok
from .vision import VisionDataset
from typing import Any, Optional

class MNIST(VisionDataset):
    urls: Any = ...
    training_file: str = ...
    test_file: str = ...
    classes: Any = ...
    @property
    def train_labels(self): ...
    @property
    def test_labels(self): ...
    @property
    def train_data(self): ...
    @property
    def test_data(self): ...
    transform: Any = ...
    target_transform: Any = ...
    train: Any = ...
    def __init__(self, root: Any, train: bool = ..., transform: Optional[Any] = ..., target_transform: Optional[Any] = ..., download: bool = ...) -> None: ...
    def __getitem__(self, index: Any): ...
    def __len__(self): ...
    @property
    def raw_folder(self): ...
    @property
    def processed_folder(self): ...
    @property
    def class_to_idx(self): ...
    @staticmethod
    def extract_gzip(gzip_path: Any, remove_finished: bool = ...) -> None: ...
    def download(self) -> None: ...
    def extra_repr(self): ...

class FashionMNIST(MNIST):
    urls: Any = ...
    classes: Any = ...

class KMNIST(MNIST):
    urls: Any = ...
    classes: Any = ...

class EMNIST(MNIST):
    url: str = ...
    splits: Any = ...
    split: Any = ...
    training_file: Any = ...
    test_file: Any = ...
    def __init__(self, root: Any, split: Any, **kwargs: Any) -> None: ...
    def download(self) -> None: ...

def get_int(b: Any): ...
def read_label_file(path: Any): ...
def read_image_file(path: Any): ...
