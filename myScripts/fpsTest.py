import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import time
import torch
from models.experimental import attempt_load
from utils.general import non_max_suppression
from utils.datasets import LoadImages
from utils.torch_utils import select_device


# Load model
device = select_device('')
model = attempt_load('../runs/train/exp133/weights/best.pt', map_location=device)
model.eval()

# Load image(s)
dataset = LoadImages('../inference/images', img_size=640)

# Warm-up
img = torch.zeros((1, 3, 640, 640), device=device)
model(img)

# FPS Testing
num_frames = 100
start_time = time.time()

for i, (path, img, im0s, vid_cap) in enumerate(dataset):
    img = torch.from_numpy(img).to(device)
    img = img.float() / 255.0
    if img.ndimension() == 3:
        img = img.unsqueeze(0)

    with torch.no_grad():
        pred = model(img)[0]
        pred = non_max_suppression(pred, 0.25, 0.45)

    if i + 1 >= num_frames:
        break

end_time = time.time()
total_time = end_time - start_time
fps = num_frames / total_time
print(f"Average FPS: {fps:.2f}")
