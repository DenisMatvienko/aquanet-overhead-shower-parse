import requests
from bs4 import BeautifulSoup


class PageDataMixin:
    """ Mixin for bs search data on each page of products  """
    def __init__(self, main_method, attrs):
        self.main_method = main_method
        self.attrs = attrs

    def find_paragraph(self):
        """ Find paragraphs & links param's on page in each product """
        try:
            return self.main_method('ul.item_props').find('li', attrs=self.attrs).find('p').find_next('p').text.strip()
        except:
            "Empty"

    def find_links(self):
        """ Find links param's on page in each product """
        try:
            return self.main_method('ul.item_props').find('li', attrs=self.attrs).find('a').text.strip()
        except:
            "Empty"


class MainPageData:
    """ Find tags & attrs on main page """
    def __init__(self, main_method, tag, attrs):
        self.main_method = main_method
        self.tag = tag
        self.attrs = attrs

    def find_main_page_data(self):
        """ Find data on main page """
        try:
            return self.main_method(self.tag).get(self.attrs)
        except:
            "Empty"




