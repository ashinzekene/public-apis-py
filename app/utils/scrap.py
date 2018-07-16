from bs4 import BeautifulSoup
import requests

def fetch_url_text(url):
    """
    Fetch for a url and return the response
    """
    return requests.get(url).text

def scrap(html, selector, attr):
    """
    Scrap for text in an html text
    """
    soup = BeautifulSoup(html, "html.parser")
    sels = soup.select(selector)
    try:
        return sels[0][attr]
    except IndexError:
        return "Not Found"


def scrap_url(url, selector, attr="src"):
    """
    For scraping web pages
    """
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    print('soup')
    print(soup)
    sels = soup.select(selector)
    try:
        urls = list(map(lambda sel: sel[attr], sels))
        print('urls')
        print(urls)
        return urls
    except IndexError:
        return "Not Found"