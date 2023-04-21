import requests
from bs4 import BeautifulSoup
def save_to_file(data, filename):
    with open(filename, 'w') as file:
        file.write(data)
def parse():
    url = 'https://omgtu.ru/general_information/faculties'
    response = requests.get(url) # выполняем GET-запрос
    soup = BeautifulSoup(response.text, 'html.parser') # создаем объект BeautifulSoup для парсинга HTML-кода страницы
    block = soup.select('div.main__content ul') # поиск элементов <ul> в разделе maincontent
    description = '' # создаем пустую строку
    for data in block: # проходим по всем элементам в переменной block
        description += data.text.strip() # добавляем текст каждого элемента <ul> с удалением пробелов в начале и конце
    return '\n'.join(filter(lambda x: x.strip(), description.split('\n'))) # удаление пустых строк
