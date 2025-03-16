import os

dataset_path = "./datasets/new_dataset/valid/labels"
for file in os.listdir(dataset_path):
    with open(os.path.join(dataset_path, file), "r") as f:
        for line in f:
            values = line.strip().split()
            if len(values) != 5:
                print(f"Error in {file}: {line}")
            else:
                class_id, x, y, w, h = map(float, values)
                if not (0 <= x <= 1 and 0 <= y <= 1 and 0 <= w <= 1 and 0 <= h <= 1):
                    print(f"Out of bounds error in {file}: {line}")
