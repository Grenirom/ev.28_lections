from bs4 import BeautifulSoup
import requests
import csv
import lxml


url = 'https://vesti.kg/'
def get_html(url):
    response = requests.get(url)
    return response.text


def get_soup(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup
get_soup(get_html)


"""
1)	В текстовом файле посчитать количество строк, а также для каждой отдельной строки определить количество в ней символов и слов.
"""

"""
2)	Спарсить vesti.kg только названия новостей(title) и записать результат в csv файл
"""