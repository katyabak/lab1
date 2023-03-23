import requests
from bs4 import BeautifulSoup
# URL страницы с факультетами
url = 'https://omgtu.ru/general_information/faculties'

# Выполнить GET-запрос к странице
response = requests.get(url)

# Создать объект BeautifulSoup для парсинга HTML-кода страницы
soup = BeautifulSoup(response.text, 'html.parser')

block = soup.select('div.main__content ul')  # находит на странице все элементы <ul> и сохраняем в контейнер
description = ''
for data in block:  # проходим циклом по содержимому контейнера
    description = data.text  # записываем в переменную содержание тега

# Записать список факультетов в файл
with open('faculties.txt', 'w') as file:
    file.write(description)