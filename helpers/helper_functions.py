import requests
from bs4 import BeautifulSoup as bs


def parse_books(items: list) -> list:
    results_ = []
    for book in items:
        title = book.find('img')['alt'].replace(',', ';')
        price = book.find('p', class_='price_color').text[2:]
        results_.append(f"{title}, {price}\n")
    return results_


def output(items: list) -> None:
    for entry in items:
        with open('data/results.csv', 'a') as f:
            f.write(entry)


def get_soup(page: int):
    url_ = f"https://books.toscrape.com/catalogue/page-{page}.html"
    page_ = requests.get(url_)
    soup = bs(page_.text, 'html.parser')
    return soup


def get_list(soup) -> list:
    books = soup.findAll('article')
    return books
