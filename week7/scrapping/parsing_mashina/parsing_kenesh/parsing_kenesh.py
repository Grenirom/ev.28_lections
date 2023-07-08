from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime
from multiprocessing import Pool



def get_html(url):
    response = requests.get(url)
    return response.text

def get_soup(html):
    soup = BeautifulSoup(html, 'lxml')
    return soup

def get_1page_links(soup):  
    links = []
    container = soup.find('div', class_='grid-deputs')
    items = container.find_all('div', class_='dep-item')
    for item in items:
        a = item.find('a').get('href')
        link = 'http://kenesh.kg' + a
        links.append(link)
    return links



def get_all_links():
    res = []
    for i in range(1,6):
        url = f'http://kenesh.kg/ru/deputy/list/35?page={i}'
        html = get_html(url)
        soup = get_soup(html)
        page_links = get_1page_links(soup)
        res.extend(page_links)
    return res


def get_deps_data(link):
    html = get_html(link)
    soup = get_soup(html)
    name = soup.find('div', class_='deput-name').text
    info =  ' '.join(soup.find('div', class_='deput-info').text.strip().split())
    # print(name)
    # print()
    # print(info)
    bio = soup.find('div', class_='tab-content').text.strip()
    img = 'http://kenesh.kg' + soup.find('div', class_='deput-image').find('img').get('src').replace(' ', '%20')
    data = {'name': name, 'info': info, 'bio': bio, 'img': img, 'link': link}
    return data

def prepare_csv():
    with open('deputy.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['FIO', 'Info', 'Bio', 'Image', 'Link to page'])

def write_to_csv(data):
    with open('deputy.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([data['name'], data['info'], data['bio'], data['img'], data['link']])
        print(f'{data["name"]} - parsed!')

def make_all(link):
    data = get_deps_data(link)
    write_to_csv(data)


def main():
    prepare_csv()
    links = get_all_links()
    # for link in links:  # последовательное выполнение
    #     data = get_deps_data(link)
    #     write_to_csv(data)

    #параллельно(многопоточно)
    with Pool(20) as pool:
        pool.map(make_all, links)


if __name__ == '__main__':
    start = datetime.now()
    main()
    finish = datetime.now()
    print(f'Parsing takes: {finish - start}!')


