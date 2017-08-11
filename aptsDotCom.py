import bs4
import urllib2
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'
}

class AptsDotCom:
    def __init__(self):
        self.url = 'https://www.apartments.com/azul-lakeshore-austin-tx/2lldd29/'
        self.page = requests.get(self.url).content
        self.soup = bs4.BeautifulSoup(self.page, 'html.parser')
        self.models = ["1A", "1C", "1F", "2A", "2B", "2C", "2D"]
        self.available = []

    def find(self):
        for model in self.models:
            status = self.soup.find("tr", {"data-model": model}).find("td", {"class": "available"}).contents[0]
            if "Available Now" in status:
                self.available.append(model)
        return self.available