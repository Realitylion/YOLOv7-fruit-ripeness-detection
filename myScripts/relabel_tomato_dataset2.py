import os

# Define paths
labels_path = "./datasets/new_dataset_2/train/labels"
print("Checking files in:", os.path.abspath(labels_path))

if not os.path.exists(labels_path):
    print(f"Error: The directory {labels_path} does not exist.")
else:
    print("Existing files:", os.listdir(labels_path))

# Mapping of old labels to new labels
label_mapping = {
    "0": "0",
    "1": "0",
    "2": "0",
    "3": "1",
    "4": "1",
    "5": "1",
}

# Iterate through label files
for label_file in os.listdir(labels_path):
    if label_file.endswith(".txt"):
        file_path = os.path.join(labels_path, label_file)

        # Read and update labels
        with open(file_path, "r") as file:
            lines = file.readlines()

        updated_lines = []
        for line in lines:
            parts = line.strip().split()
            if parts:
                old_label = parts[0]
                if old_label in label_mapping:
                    parts[0] = label_mapping[old_label]  # Update label
                    updated_lines.append(" ".join(parts))

        # Write updated labels back to file
        with open(file_path, "w") as file:
            file.write("\n".join(updated_lines) + "\n")

print("Labels successfully updated to 'ripe' (0) and 'unripe' (1).")
