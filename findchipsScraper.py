from bs4 import BeautifulSoup
from urllib.request import urlopen


# Call findchips with search parameter
def search_chip(part_number):
    url="https://www.findchips.com/search/"
    page = urlopen(url+part_number)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    results = soup.find_all(class_='distributor-results')
    filename = "chip.html"
    with open(filename, "w", encoding="utf-8") as file:
        for result in results:
            file.write(str(result.contents[3]))
    file.close()
    return file
    
#search_chip("sn75468d")