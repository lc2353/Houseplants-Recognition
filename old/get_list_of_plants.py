import requests
from bs4 import BeautifulSoup

# send a GET request to the website
url = "https://www.guide-to-houseplants.com/house-plants-encyclopedia-a-z.html"
response = requests.get(url)

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# find all the <a> tags within the div with id="content-area"
content_area = soup.find("div", {"id": "ContentColumn"})
links = content_area.find_all("a")


# extract the name of each houseplant from the <a> tag and print it
with open("plants.txt", "w") as f:
    for link in links:
        name = link.text.strip()
        f.write(name + "\n")