import requests
from bs4 import BeautifulSoup

def get_scraped_data(url):
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return [], [], []

    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract headings (h1, h2, h3 tags)
    headings = soup.find_all(['h1', 'h2', 'h3'])

    # Extract all links
    links = [a.get('href') for a in soup.find_all('a', href=True)]

    # Extract all images
    images = [img.get('src') for img in soup.find_all('img', src=True)]

    return headings, links, images
