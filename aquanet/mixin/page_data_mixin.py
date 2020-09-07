import requests
from bs4 import BeautifulSoup


class PageDataMixin:
    """ Mixin for bs search data  """
    def __init__(self, main_method, attrs, tag2, attrs2, tag3):
        self.main_method = main_method
        self.attrs = attrs
        self.tag2 = tag2
        self.attrs2 = attrs2
        self.tag3 = tag3

    def find_paragraph(self):
        """ Find paragraphs """
        try:
            return self.main_method(self.attrs).find(self.tag2, attrs=self.attrs2).find(self.tag3) \
                .find_next(self.tag3).text
        except:
            "Empty"





