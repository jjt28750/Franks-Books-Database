## Web Scraper
## Jalen Tam
##
## This web scraper is used to get data to populate my inventory database.

## Import Python libraries
import requests
from bs4 import BeautifulSoup

## function: scrape()
## Gets information from HTML code on webpage.
def scrape():

    ## URL getting information from
    url = 'https://books.toscrape.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find(class_='col-sm-8 col-md-9')

    bookCard = results.find_all("li", class_ = "col-xs-6 col-sm-4 col-md-3 col-lg-3")
    for book in bookCard:
        title = book.find("h3")
        price = book.find("p", class_="price_color")
        
        print(title.text.strip())
        print(price.text.strip())
    

if __name__ == '__main__':
    scrape()