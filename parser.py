from bs4 import BeautifulSoup

import random
import requests
import pandas as pd
import numpy as np
import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def user_agent():

    headers = ['Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0',
               'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
               'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
               'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11) AppleWebKit/601.1.56 (KHTML, like Gecko) Version/9.0 Safari/601.1.56',
               'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/601.2.7 (KHTML, like Gecko) Version/9.0.1 Safari/601.2.7',
               'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
               'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0',
               'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0',
               'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0',
               'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:41.0) Gecko/20100101 Firefox/41.0',
               'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
               'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
               'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36',
               'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
               ]
    return {'User-Agent': headers[random.randrange(0, len(headers))]}

def clearing(text):
    reg1 = re.compile('\[.*?]')
    reg2 = re.compile('\(.*?\)')
    return ''.join(re.findall('[\d]', reg2.sub('', reg1.sub('', str(text)))))

url1 = 'https://ru.wikipedia.org/wiki/'
url2 = 'https://www.list-org.com/search?val=СНТ+'
url2_base = 'https://www.list-org.com'
cities = [
    'Калининград', 'Славск', 'Гвардейск', 'Багратионовск',
    'Большое_Исаково', 'Зеленоградск', 'Правдинск', 'Черняховск',
    'Полесск', 'Ладушкин', 'Мамоново', 'Малое_Исаково', 'Янтарный',
    'Шоссейное', 'Домново'
]

def get_snt(snt):
    response = requests.get(f'{url2}{snt.split(" ")[1]}&type=name&work=on&okato=27&okved=68.32.2', headers=user_agent())
    soup = BeautifulSoup(response.content, features="lxml")
    print(f"{url2_base}{soup.find('label').find('a',  href=True)['href']}")

    browser.get(f"{url2_base}{soup.find('label').find('a', href=True)['href']}")
    html = browser.page_source
    soup2 = BeautifulSoup(html, features="lxml")

    return pd.read_html(soup2.find('table', class_='table table-sm').decode())[0]

def get_city(city):
    city = city.replace(' ', '_')
    print(city)
    if city == 'Гусев':
        response = requests.get(f'{url1}{city}о_(Калининградская_область)', headers=user_agent())
    elif city == 'Невское' or city == 'Луговое' or city == 'Матросово' or city == 'Некрасово' or city == 'Родники':
        response = requests.get(f'{url1}{city}_(Гурьевский_район)', headers=user_agent())
    elif city == 'Малиновка' or city ==  'Озерки':
        response = requests.get(f'{url1}{city}_(Гвардейский_район)', headers=user_agent())
    elif city == 'Первомайское':
        response = requests.get(f'{url1}{city}_(Гусевский район)', headers=user_agent())
    elif city == 'Неман' or city == 'Пионерский':
        response = requests.get(f'{url1}{city}_(город)', headers=user_agent())
    elif city in cities:
        response = requests.get(f'{url1}{city}', headers=user_agent())
    elif city == 'Садовое':
        response = requests.get(f'{url1}{city[:-1]}_(Калининградская_область)', headers=user_agent())
    elif city == 'Сосновка' or city == 'Славянское':
        response = requests.get(f'{url1}{city}_(Полесский_район)', headers=user_agent())
    elif city == 'Раздольное' or city == 'Березовка':
        response = requests.get(f'{url1}{city}_(Багратионовский_район)', headers=user_agent())
    elif city == 'Высокое' or city == 'Тимирязево':
        response = requests.get(f'{url1}{city}_(Славский_район)', headers=user_agent())
    elif city == 'Кумачево' or city == 'Рощино':
        response = requests.get(f'{url1}{city.replace("е", "ё")}_(Зеленоградский район)', headers=user_agent())
    elif city == 'Новодорожный':
        response = requests.get(f'{url1}Ново-Дорожный', headers=user_agent())
    elif city == 'Новостроево':
        response = requests.get(f'{url1}{city}_(Правдинский_район)', headers=user_agent())
    elif city == 'Пригородное':
        response = requests.get(f'{url1}{city}_(Нестеровский_район)', headers=user_agent())
    elif city == 'Партизанское':
        response = requests.get(f'{url1}{city}_(Черняховский_район)', headers=user_agent())
    else:
        response = requests.get(f'{url1}{city}_(Калининградская_область)', headers=user_agent())
    soup = BeautifulSoup(response.content, features="lxml")
    if city == 'Советск':
        return pd.read_html(soup.find_all('table')[1].decode())[0]
    return pd.read_html(soup.find('table').decode())[0]

def get_c(town):
    if town.startswith('СТ') and town != 'СТ Радуга':
        res = get_snt(town)

        res = res[res.columns[1]][res[res.columns[0]] == 'Количество учредителей:']
        print(res)
    elif town == 'СТ Радуга':
        res = pd.Series([1])
    else:
        res = get_city(town)
        res[1] = res[1].apply(clearing)
        print(res[1][(res[0] == 'Население') & (res[1] != '')].values, res[1][(res[0] == 'Население') & (res[1] != '')] )
        res = res[1][(res[0] == 'Население') & (res[1] != '')]
    return res.values[0]


train = pd.read_csv('train_dataset_train.csv', sep=';', index_col=None,
                    dtype={'PATIENT_SEX': str, 'MKB_CODE': str, 'ADRES': str, 'VISIT_MONTH_YEAR': str,
                           'AGE_CATEGORY': str, 'PATIENT_ID_COUNT': int})
test = pd.read_csv('test_dataset_test.csv', sep=';', index_col=None,
                   dtype={'PATIENT_SEX': str, 'MKB_CODE': str, 'ADRES': str, 'VISIT_MONTH_YEAR': str,
                          'AGE_CATEGORY': str})

browser = webdriver.Chrome(ChromeDriverManager().install())
train = train.drop(columns=['PATIENT_ID_COUNT']).append(test)
list_ = []
for i in train['ADRES'].unique():
    if len(train[train['ADRES'] == i]['VISIT_MONTH_YEAR'].unique()) == 52 or i.startswith('СТ'):
        list_.append(i)
train = train[train['ADRES'].isin(list_)]
weather = pd.DataFrame(pd.Series(train['ADRES'].unique()).apply(get_c), columns=['COUNT'])
weather.insert(0, 'ADRES', train['ADRES'].unique())
print(weather)
weather.to_csv('counts.csv')
browser.close()
