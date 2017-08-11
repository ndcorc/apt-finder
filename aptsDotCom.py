import bs4
import urllib2

class AptsDotCom:
    def __init__(self):
        self.url = 'https://www.apartments.com/azul-lakeshore-austin-tx/2lldd29/'
        self.req = urllib2.Request(self.url, headers={'User-Agent' : "Magic Browser"})
        self.page = urllib2.urlopen(self.req)
        self.soup = bs4.BeautifulSoup(self.page.read(), 'html.parser')
        self.models = ["1A", "1C", "1F", "2A", "2B", "2C", "2D"]
        self.available = []

    def find(self):
        for model in self.models:
            status = self.soup.find("tr", {"data-model": model}).find("td", {"class": "available"}).contents[0]
            if "Available Now" in status:
                self.available.append(model)
        return self.available