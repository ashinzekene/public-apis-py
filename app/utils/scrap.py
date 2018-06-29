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
    sel = soup.select(selector)
    if sel == None or sel[0] == None:
        return "Not Found"
    return sel[0][attr]

def scrap_url(url, selector, attr="src"):
    """
    For scraping web pages
    """
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    print(soup)
    sel = soup.select(selector)
    if sel == None or sel[0] == None:
        return "Not Found"
    return sel[0][attr]