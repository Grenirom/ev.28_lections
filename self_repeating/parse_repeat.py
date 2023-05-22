from typing import Any
import requests
from bs4 import BeautifulSoup
                #TASK 6

url = 'https://www.imdb.com/chart/top'
html = requests.get(url).text
soup = BeautifulSoup(html, 'lxml')
links = []
def get_link():
    container = soup.find_all('tr')
    # link = container.find('a').get('href')
    print(container)

get_link()


class A:
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass

            

















# url = requests.get('https://enter.kg/').text
# soup = BeautifulSoup(url, 'lxml')
# container = soup.find('ul', class_='VMmenu')
# category_list = [x.text for x in container.find_all('a')]
# # print(category_list)
# def find_cat(categories, keyword):
#         return  [x for x in categories if keyword.lower() in x.lower()]
# print(find_cat(category_list, 'ноутбуки' ))

# def getTitle(url): 
#     response= requests.get(url).text 
#     soup = BeautifulSoup(response, 'lxml') 
#     i= soup.find('h1') 
#     if i: 
#         return i 
#     else : 
#         return "Title could not be found" 
# print(getTitle('http://www.example.com/'))





# import lxml
# import csv



# def get_html(url):
#     ressponse = requests.get(url)
#     print(ressponse.status_code)



# def main():
#     laptops_url = 'https://www.eldorado.ru/c/noutbuki/'
#     page_link = '?page='
#     get_html(laptops_url)

# main()