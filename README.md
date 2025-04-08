# 🍌🍎 Towards Automated Agriculture: A Computer Vision Approach for Fruit Ripeness Detection


This project focuses on detecting the ripeness of fruits using object detection models. We compare the baseline **YOLOv7** model with a custom **YOLOv7-BiFPN** variant to evaluate performance on a dataset annotated with ripeness labels.

## 🔍 Objective

To accurately detect and classify fruits (apple, banana, damson plum, mango, and orange) based on their ripeness state (ripe/unripe) using computer vision and deep learning.

---

## 📦 Dataset Details

- **Total Images:** 195 (original), augmented to 585
- **Augmentation Techniques:**
  - Horizontal Flip
  - Brightness Adjustment: -25% to +25%
  - Gaussian Blur: up to 2.5px
- **Annotation Format:** YOLO
- **Labeling Strategy:**
  - One kind of fruit per image (can have multiple instances)
  - Fruits: `apple`, `banana`, `damson plum`, `mango`, `orange`
  - Each fruit annotated individually, except bananas (a bunch treated as a single entity)
  - Labels: `ripe`, `unripe`
- **Train/Val Split:** 80:20

---

## 🧠 Models

### ✅ YOLOv7 (Baseline)
- Standard YOLOv7 architecture

### 🔁 YOLO-BiFPN (Custom)
- Modified **SPPCSPC** module in YOLOv7 head replaced with **BiFPN** (Bidirectional Feature Pyramid Network)
- Custom **loss function** including:
  - **Focal Loss**: Addresses class imbalance
  - **Dice Loss**: Improves segmentation and localization accuracy

---

## 🧪 Hyperparameters & Environment

### 🖥️ Hardware & System

- **Laptop:** Lenovo Legion 5
- **Processor:** AMD Ryzen 7 7940HS
- **RAM:** 16 GB
- **GPU:** 6 GB VRAM (NVIDIA, CUDA enabled)
- **Training Framework:** NVIDIA CUDA Toolkit (for GPU acceleration)

### ⚙️ Hyperparameters (Common to Both Models)

| Parameter      | Value       |
|----------------|-------------|
| Batch Size     | 2           |
| Epochs         | 30          |
| Image Size     | 640 × 640   |
| Optimizer      | SGD (YOLO default) |
| Loss Function  | YOLOv7 default (for baseline) / Custom with Focal + Dice Loss (for YOLO-BiFPN) |
| Augmentations  | Flip, Brightness, Blur (handled via Roboflow) |

> ⚡ Both models were trained using GPU acceleration powered by NVIDIA CUDA software to optimize training time and performance.

---

## 📊 Results

| Model         | Precision | Recall | mAP@0.5 | mAP@0.5:0.95 | F1 Score |
|---------------|-----------|--------|---------|--------------|----------|
| YOLOv7        | 0.868     | 0.784  | 0.876   | 0.694        | 0.8238   |
| YOLOv7-BiFPN  | 0.92      | 0.858  | 0.925   | 0.764        | 0.8879   |

> 🔍 **Observation:** The modified YOLO-BiFPN consistently outperforms the baseline YOLOv7 model across all key metrics

---

## 🛠 Tools & Libraries Used

- YOLOv7 (Ultralytics)
- Roboflow (for labeling & augmentation)
- PyTorch
- OpenCV

---

## 📌 Future Work

- Extend dataset to include more fruit types and ripeness stages
- Explore multi-label classification (e.g. ripe + damaged)

---

## 📷 Sample Output 

- Confidence threshold set to 0.7
- YOLOv7
![YOLOv7-1](test4.jpg)

- YOLOv7-BiFPN
![YOLOv7-BiFPN-1](test4-1.jpg)

- We can see in this example that the modified YOLOv7-BiFPN model is able to detect occluded as well as partially visible fruits precisely, while the base model can not

---

## ✨ Acknowledgements

- [YOLOv7 by WongKinYiu](https://github.com/WongKinYiu/yolov7)
- [Roboflow](https://roboflow.com/) for easy dataset handling

---

