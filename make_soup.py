import requests
from bs4 import BeautifulSoup


def get_html(url):
    rec = requests.get(url)
    rec.encoding = rec.apparent_encoding
    return rec.text


def make_soup(url):
    return BeautifulSoup(get_html(url), 'lxml')


if __name__ == '__main__':
    make_soup('https://languagedrops.com/word/en/english/hebrew/')
