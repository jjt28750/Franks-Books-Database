## Web Scraper
## Jalen Tam
##
## This web scraper is used to get data to populate my inventory database.
import requests
from bs4 import BeautifulSoup

def scrape():

    url = 'https://books.toscrape.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find(class_='col-sm-8 col-md-9')
    

if __name__ == '__main__':
    scrape()