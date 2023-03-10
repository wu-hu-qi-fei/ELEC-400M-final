from typing import List, Dict
from . import transforms as T

def build_transforms(cfg_transforms: List[Dict] = None):

    if cfg_transforms is None:
        transforms = T.Compose([
            T.ToTensor()
        ])
    else:
        transform_list = []
        for t in cfg_transforms:
            transform_list.append(getattr(T, t["name"])(**t["args"]))
        transforms = T.Compose(transform_list)
    
    return transforms
