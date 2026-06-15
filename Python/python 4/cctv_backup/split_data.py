import os
import random
import shutil

train_images_path = 'datasets_video/train/images'
train_labels_path = 'datasets_video/train/labels'
valid_images_path = 'datasets_video/valid/images'
valid_labels_path = 'datasets_video/valid/labels'

split_percentage = 0.2  # 20%

os.makedirs(valid_images_path, exist_ok=True)
os.makedirs(valid_labels_path, exist_ok=True)

images = [f for f in os.listdir(train_images_path) if f.endswith(('.jpg', '.jpeg', '.png'))]
random.shuffle(images)

num_to_move = int(len(images) * split_percentage)

images_to_move = images[:num_to_move]

moved_count = 0
for image_name in images_to_move:
    base_name = os.path.splitext(image_name)[0]
    
    if base_name != "classes": 
        label_name = base_name + '.txt'

        src_image_path = os.path.join(train_images_path, image_name)
        src_label_path = os.path.join(train_labels_path, label_name)

        dest_image_path = os.path.join(valid_images_path, image_name)
        dest_label_path = os.path.join(valid_labels_path, label_name)

        if os.path.exists(src_image_path) and os.path.exists(src_label_path):
            shutil.move(src_image_path, dest_image_path)
            shutil.move(src_label_path, dest_label_path)
            moved_count += 1
            print(f"Moved {image_name} and {label_name} to validation set.")
        else:
            print(f"Warning: Could not find corresponding label for {image_name}. Skipping.")

print(f"\nProcess complete. Moved {moved_count} image/label pairs to the validation set.")
