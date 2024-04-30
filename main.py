from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests
def parse():
    url = 'https://steamcommunity.com/market/search?appid=730' # передаем необходимы URL адрес
    page = requests.get(url) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    #print(page.status_code) # смотрим ответ
    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4
    block = soup.find('div', id='searchResultsRows') # находим  контейнер с нужным классом
    items = block.findAll('a', class_='market_listing_row_link')
    description = ''
    a = 1
    for item in items: # проходим циклом по содержимому контейнера
        print(a, 'Предмет')
        name = item.find('span', class_='market_listing_item_name').text
        print('Название: ', name)
        price = item.find('span', class_='sale_price').text
        print('Цена: ', price)
        num = item.find('span', class_='market_listing_num_listings_qty').text
        print('Количество: ', num, '\n')
        print('_____________________________________')
        a += 1

parse()