import os
import numpy as np
from PIL import Image

data_root = os.path.expanduser("~/data")

main_corruptions = [
    'gaussian_noise', 'shot_noise', 'impulse_noise', 'defocus_blur',
    'glass_blur', 'motion_blur', 'zoom_blur', 'snow', 'frost', 'fog',
    'brightness', 'contrast', 'elastic_transform', 'pixelate', 'jpeg_compression',
]

def make_numpy_dataset(dataset_name, img_size=(32, 32, 3)):
    path = os.path.join(data_root, "corruption", dataset_name)
    os.makedirs(path, exist_ok=True)
    N = 1
    total = N * 5
    labels = np.zeros(total, dtype=np.int64)
    np.save(os.path.join(path, "labels.npy"), labels)
    for c in main_corruptions:
        imgs = np.zeros((total,) + img_size, dtype=np.uint8)
        np.save(os.path.join(path, f"{c}.npy"), imgs)

make_numpy_dataset("CIFAR-10-C")
make_numpy_dataset("CIFAR-100-C")

def make_imagenet_c():
    path = os.path.join(data_root, "corruption", "ImageNet-C")
    os.makedirs(path, exist_ok=True)
    
    with open(os.path.join(path, "classnames.txt"), "w") as f:
        f.write("cls0 dummy_class\n")
        
    for c in main_corruptions:
        img_path = os.path.join(path, c, "5", "cls0")
        os.makedirs(img_path, exist_ok=True)
        img = Image.fromarray(np.zeros((224, 224, 3), dtype=np.uint8))
        img.save(os.path.join(img_path, "dummy.jpg"))

make_imagenet_c()

def make_domainnet():
    path = os.path.join(data_root, "domainbed", "domain_net")
    os.makedirs(path, exist_ok=True)
    envs = ['clipart', 'infograph', 'painting', 'quickdraw', 'real', 'sketch']
    for e in envs:
        img_path = os.path.join(path, e, "cls0")
        os.makedirs(img_path, exist_ok=True)
        img = Image.fromarray(np.zeros((224, 224, 3), dtype=np.uint8))
        img.save(os.path.join(img_path, "dummy.jpg"))

make_domainnet()

print("Dummy dataset generated successfully.")
