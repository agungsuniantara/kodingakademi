import os
import random
import shutil

# Define paths
train_images_path = 'datasets/data_kustom/train/images'
train_labels_path = 'datasets/data_kustom/train/labels'
valid_images_path = 'datasets/data_kustom/valid/images'
valid_labels_path = 'datasets/data_kustom/valid/labels'

# Define the percentage of data to move to the validation set
split_percentage = 0.2  # 20%

# Create validation directories if they don't exist
os.makedirs(valid_images_path, exist_ok=True)
os.makedirs(valid_labels_path, exist_ok=True)

# Get the list of all image files in the training directory
images = [f for f in os.listdir(train_images_path) if f.endswith(('.jpg', '.jpeg', '.png'))]
random.shuffle(images)

# Calculate the number of images to move
num_to_move = int(len(images) * split_percentage)

# Select images to move
images_to_move = images[:num_to_move]

# Move the selected images and their corresponding labels
moved_count = 0
for image_name in images_to_move:
    # Construct file paths
    base_name = os.path.splitext(image_name)[0]
    label_name = base_name + '.txt'

    src_image_path = os.path.join(train_images_path, image_name)
    src_label_path = os.path.join(train_labels_path, label_name)

    dest_image_path = os.path.join(valid_images_path, image_name)
    dest_label_path = os.path.join(valid_labels_path, label_name)

    # Check if both image and label files exist before moving
    if os.path.exists(src_image_path) and os.path.exists(src_label_path):
        # Move the files
        shutil.move(src_image_path, dest_image_path)
        shutil.move(src_label_path, dest_label_path)
        moved_count += 1
        print(f"Moved {image_name} and {label_name} to validation set.")
    else:
        print(f"Warning: Could not find corresponding label for {image_name}. Skipping.")

print(f"\nProcess complete. Moved {moved_count} image/label pairs to the validation set.")
