import os

# Define paths
labels_path = "./datasets/tomato_dataset_augmented/labels"

# Mapping of old labels to new labels
label_mapping = {
    "0": "4",  # ripe -> Ripe_Tomato
    "1": "5",  # unripe -> Raw_Tomato
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
