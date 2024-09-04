from bs4 import BeautifulSoup
from urllib.request import urlopen

class chip:
    # Call findchips with search parameter
    def search_chip(self):
        url="https://www.findchips.com/search/"
        page = urlopen(url+self.part_number)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        results = soup.find_all(class_='distributor-results')
        filename = "chip.html"
        with open(filename, "w", encoding="utf-8") as file:
            for result in results:
                file.write(str(result.contents[3]))
        file.close()
        return file
    
    def __init__(self, part_number):
        self.part_number = part_number