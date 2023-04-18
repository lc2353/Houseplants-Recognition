import requests
from bs4 import BeautifulSoup
import os

# Define a list of plant names to search for
plant_names = []
with open("dataset_config/plants.txt", "r") as p:
    for line in p:
        plant_names.append(line.strip())

# Create a directory to store the images
parent_dir = "dataset_config/plant_images"
if not os.path.exists(parent_dir):
    os.makedirs(parent_dir)

# Loop through the plant names and download the first image of the search results
for plant_name in plant_names:

    # Create a subdirectory for each plant
    directory = os.path.join(parent_dir, plant_name)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Construct the search query URL
    query_url = f'https://www.google.com/search?q={plant_name}+house+plant&tbm=isch'

    # Send an HTTP GET request to the query URL and parse the response with BeautifulSoup
    response = requests.get(query_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the first 5 image URLs in the search results and download the images
    image_urls = []
    for img in soup.find_all('img'):
        if 'http' in img['src']:
            image_urls.append(img['src'])
            if len(image_urls) == 6:
                break

    for i, url in enumerate(image_urls):
        try:
            response = requests.get(url)
            filename = os.path.join(directory, f"{plant_name}_{i}.jpg")
            with open(filename, "wb") as f:
                f.write(response.content)
            print(f"Downloaded {plant_name} image {i+1}.")
        except:
            print(f"Error downloading {plant_name} image {i+1}.")
