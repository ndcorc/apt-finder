import bs4
import urllib2 as url


class AptFinder:
    def __init__(self):
        self.page = url.urlopen('http://www.apartmentfinder.com/Texas/Austin-Apartments/Azul-Lakeshore-Apartments')
        self.soup = bs4.BeautifulSoup(self.page.read(), 'html.parser')
        self.models = ["1F", "2A", "2B", "2C", "2D"]
        self.available = []

    def find(self):
        for model in self.models:
            status = self.soup.find("div", {"data-model": model}).find("div", {"class": "available"}).contents[0]
            if "Available Now" in status:
                self.available.append(model)
        return self.available