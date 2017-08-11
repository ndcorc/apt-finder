import bs4
import urllib2

class AptFinder:
    def __init__(self):
        self.url = 'http://www.apartmentfinder.com/Texas/Austin-Apartments/Azul-Lakeshore-Apartments'
        self.req = urllib2.Request(self.url, headers={'User-Agent' : "Magic Browser"})
        self.page = urllib2.urlopen(self.req)
        self.soup = bs4.BeautifulSoup(self.page.read(), 'html.parser')
        self.models = ["1A", "1C", "1F", "2A", "2B", "2C", "2D"]
        self.available = []

    def find(self):
        for model in self.models:
            status = self.soup.find("div", {"data-model": model}).find("div", {"class": "available"}).contents[0]
            if "Available Now" in status:
                self.available.append(model)
        return self.available