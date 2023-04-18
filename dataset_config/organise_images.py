import os
from PIL import Image

# Define the paths for the original and resized images
original_images_path = "dataset_config/pothos_images"
new_images_path = "pothos_dataset"

# Loop through all the plant folders in the original images path
for plant_folder in os.listdir(original_images_path):
    if plant_folder == '.DS_Store':
        continue

    plant_path = os.path.join(original_images_path, plant_folder)

    # Create subfolders for training and test
    training_path = os.path.join(new_images_path, "training", plant_folder)
    test_path = os.path.join(new_images_path, "test", plant_folder)
    os.makedirs(training_path, exist_ok=True)
    os.makedirs(test_path, exist_ok=True)

    # Loop through all the images in the plant folder
    images = os.listdir(plant_path)
    for i, image in enumerate(images):
        # Resize the image using your preferred method
        img = Image.open(os.path.join(plant_path, image))
        # Save the resized image to the appropriate folder (training or test)
        if i < 3:
            destination_path = os.path.join(
                training_path, f"{plant_folder}_{image}")
        else:
            destination_path = os.path.join(
                test_path, f"{plant_folder}_{image}")
        img.save(destination_path)

        # Remove the resized image object from memory
        del img

    print("Successfully resized images for plant: " + plant_folder)
