from bs4 import BeautifulSoup
import requests

class RecipePuller:
    def __init__(self, url):
        self.url = url

    def process(self):
        try:
            r = requests.get(self.url)
            data = r.text
            soup = BeautifulSoup(data)
            title = soup.find(id="itemTitle")
            print title.text
            for ingredient in soup.find_all(id="liIngredient"):
                amt = ingredient.find(id="lblIngAmount")
                name = ingredient.find(id="lblIngName")
                if amt is not None:
                    print "\t" + amt.text + " " + name.text
                elif name.text:
                    print "\t" + name.text
            directions = soup.find("div", class_="directLeft")
            for direction in directions.find_all("li"):
                print direction.find("span").text
        except Exception as e:
            print e
