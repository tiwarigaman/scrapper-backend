from bs4 import BeautifulSoup
import requests

def get_scraped_data(url):
    response = requests.get(url)
    if response.status_code != 200:
        return [], [], []

    soup = BeautifulSoup(response.content, 'html.parser')
    headings = soup.find_all('h1')
    links = soup.find_all('a')
    images = soup.find_all('img')

    return headings, links, images
