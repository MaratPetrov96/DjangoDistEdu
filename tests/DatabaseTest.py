from django.test import TestCase
from MainApp.models import *
from transliterate import slugify
from bs4 import BeautifulSoup as bs
import requests as req

test_title = 'Автоматизированные системы управления'

url = 'https://base.garant.ru/70480868/53f89421bbdaf741eb2d1ecc4ddb4c33/'

main = bs(req.get(url,'html.parser').text,features='lxml')

data_for_test = []

for i in main.findAll(class_='s_16'):
    if i.findPrevious('p').text.endswith('.00'):
        dct = dict()
        dct['code'] = i.findPrevious('p').text[:2]
        dct['title'] = i.findNext(class_='s_16').text.capitalize()
        dct['url'] = slugify(dct['title'])
        data_for_test.append(dct)
        

class FirstTest(TestCase):
    def add_data(self):
        Cathedra.objects.create(title=test_title, abbreviation="АСУ")
        for dct in data_for_test:
            Stream.objects.create(
                title=dct['title'],
                url=slugify(dct['title']),
                code=dct['code']
            )
