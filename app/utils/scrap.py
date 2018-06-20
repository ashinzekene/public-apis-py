from bs4 import BeautifulSoup
import requests

def scrap(url, selector, multiple):
    """
    For scraping web pages
    """
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    print(soup)
    sel = soup.find(selector)
    if sel == None:
        return "Not Found"
    return sel["src"]
