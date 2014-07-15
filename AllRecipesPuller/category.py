import sys
import requests
from recipe import RecipePuller
from bs4 import BeautifulSoup

class CategoryPuller:
    def __init__(self, url):
        self.url = url
        self.page = 1

    def process(self):
        try:
            r = requests.get(self.url+"&Page="+str(self.page))
            data = r.text
            soup = BeautifulSoup(data)
            for recipe in soup.find_all(id="divGridItemWrapper"):
                a = recipe.find('a')
                r = RecipePuller("http://allrecipes.com"+a.get('href'))
                r.process()
            self.page += 1
            self.process()
        except Exception as e:
            print e
