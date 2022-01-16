import requests
from bs4 import BeautifulSoup
import main
import html5lib


class Products():


    def __init__(self):

        self.Product_name = ""
        self.url_interdiscount = "https://www.interdiscount.ch/de/search?search="


    def get_product_name(self):

        self.page = requests.get(self.main.url_interdiscount)
        self.html = BeautifulSoup(self.page.text, "html5lib")
        self.Product_name = self.html.find(class_="uIyEJC _2sh9pz _2mLeUk _9YoDdk")["title"]
