from bs4 import BeautifulSoup

import requests
import csv

CSV = 'dict.csv'
HOST = 'http://nati.org.ua'
URL = 'http://nati.org.ua/node/516'
HEADERS = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }


def get_html(url):
    r = requests.get(url, headers=HEADERS)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')

    items = soup.find('div', class_='node')
    links = items.find('div', class_='').find_all('a')

    dict = []

    for item in links:
        dict.append(
            {
                'link': item.get('href')
            }
        )
    return dict


def save(links, CSV):
    with open("parsing/second/link_pars.csv", 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Ссылка на продукт'])
        for item in links:
            writer.writerow(([item['link']]))


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        dict = []
        for node in range(1):
            print(f'Парсим страницу {node}')
            html = get_html(URL)
            dict.extend(get_content(html.text))
            save(dict, CSV)
        print("Пасрсинг закончился")
    else:
        print('Ошибка бро')


parser()

