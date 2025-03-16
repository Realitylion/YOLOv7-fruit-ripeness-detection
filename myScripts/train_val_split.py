import os
import shutil
from sklearn.model_selection import train_test_split

# Define dataset paths
dataset_path = os.path.abspath("datasets/new_dataset_2")  # Absolute path
images_path = os.path.join(dataset_path, "images")
labels_path = os.path.join(dataset_path, "labels")

train_path = os.path.join(dataset_path, "train")
val_path = os.path.join(dataset_path, "val")

# Create train/val directories if they don’t exist
for split in ["train", "val"]:
    os.makedirs(os.path.join(train_path, "images"), exist_ok=True)
    os.makedirs(os.path.join(train_path, "labels"), exist_ok=True)

# Get list of all image files
image_files = [f for f in os.listdir(images_path) if f.endswith((".jpg", ".png", ".jpeg"))]

# Split dataset using sklearn's train_test_split
train_files, val_files = train_test_split(image_files, test_size=0.2, random_state=42)

# Function to move files safely
def move_files(file_list, split):
    for img_file in file_list:
        img_src = os.path.join(images_path, img_file)
        lbl_src = os.path.join(labels_path, img_file.replace(".jpg", ".txt").replace(".png", ".txt").replace(".jpeg", ".txt"))

        img_dest = os.path.join(dataset_path, split, "images", img_file)
        lbl_dest = os.path.join(dataset_path, split, "labels", os.path.basename(lbl_src))

        # Move only if file exists
        if os.path.exists(img_src):
            shutil.move(img_src, img_dest)
        else:
            print(f"⚠️ Warning: {img_src} not found!")

        if os.path.exists(lbl_src):
            shutil.move(lbl_src, lbl_dest)
        else:
            print(f"⚠️ Warning: {lbl_src} not found!")

# Move files to train/val folders
move_files(train_files, "train")
move_files(val_files, "val")

print("✅ Dataset split into 80% train and 20% val successfully!")