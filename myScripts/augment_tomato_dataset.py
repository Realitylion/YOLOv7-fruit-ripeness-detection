import os
import cv2

# Define paths
images_path = "./datasets/tomato_dataset_unaugmented/images"  # Folder containing original images
labels_path = "./datasets/tomato_dataset_unaugmented/labels"  # Folder containing original YOLO labels
output_images_path = "./datasets/tomato_dataset_augmented/images"  # Output folder for flipped images
output_labels_path = "./datasets/tomato_dataset_augmented/labels"  # Output folder for flipped labels

# Create output folders if they don't exist
os.makedirs(output_images_path, exist_ok=True)
os.makedirs(output_labels_path, exist_ok=True)

# Process all images in the dataset
for img_file in os.listdir(images_path):
    if img_file.endswith((".jpg", ".jpeg", ".png")):
        img_path = os.path.join(images_path, img_file)
        label_path = os.path.join(labels_path, img_file.replace(".jpg", ".txt").replace(".png", ".txt").replace(".jpeg", ".txt"))
        
        # Read the image
        image = cv2.imread(img_path)
        h, w = image.shape[:2]

        # Flip the image horizontally
        flipped_image = cv2.flip(image, 1)

        # Save flipped image
        flipped_img_name = img_file.replace(".", "_flipped.")
        flipped_img_path = os.path.join(output_images_path, flipped_img_name)
        cv2.imwrite(flipped_img_path, flipped_image)

        # Process corresponding YOLO label file
        if os.path.exists(label_path):
            with open(label_path, "r") as file:
                lines = file.readlines()

            flipped_labels = []
            for line in lines:
                parts = line.strip().split()
                if len(parts) == 5:
                    class_id, x_center, y_center, width, height = parts
                    x_center = float(x_center)
                    
                    # Flip X-coordinate (1 - current x)
                    new_x_center = 1.0 - x_center
                    flipped_labels.append(f"{class_id} {new_x_center:.6f} {y_center} {width} {height}")

            # Save flipped labels
            flipped_label_name = img_file.replace(".", "_flipped.").replace(".jpg", ".txt").replace(".png", ".txt").replace(".jpeg", ".txt")
            flipped_label_path = os.path.join(output_labels_path, flipped_label_name)
            
            with open(flipped_label_path, "w") as file:
                file.write("\n".join(flipped_labels) + "\n")

print("✅ Dataset augmentation complete! Flipped images and labels saved.")
