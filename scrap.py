import requests
from bs4 import BeautifulSoup

def get_scraped_data():
    url = 'https://www.amazon.in'
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return [], []

    soup = BeautifulSoup(response.content, 'html.parser')
    headings = soup.find_all('h1')
    links = soup.find_all('a')

    return headings, links
