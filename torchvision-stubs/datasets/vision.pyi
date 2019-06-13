# Stubs for torchvision.datasets.vision (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import torch.utils.data as data
from typing import Any, Optional

class VisionDataset(data.Dataset):
    root: Any = ...
    transform: Any = ...
    target_transform: Any = ...
    transforms: Any = ...
    def __init__(self, root: Any, transforms: Optional[Any] = ..., transform: Optional[Any] = ..., target_transform: Optional[Any] = ...) -> None: ...
    def __getitem__(self, index: Any) -> None: ...
    def __len__(self) -> None: ...
    def extra_repr(self): ...

class StandardTransform:
    transform: Any = ...
    target_transform: Any = ...
    def __init__(self, transform: Optional[Any] = ..., target_transform: Optional[Any] = ...) -> None: ...
    def __call__(self, input: Any, target: Any): ...