import sys
import requests
from bs4 import BeautifulSoup

print('[1] - Importar palabras clave')
print('[2] - Mostrar palabras clave')
print('[3] - Comprobar palabras clave')
print('[0] - Salir')


def read_option():
    """Read option."""
    return input()


def load_keywords():
    """
    Load Keywords.
    :return:
        List with words
    """
    keys = []
    with open('keywords.txt', 'r') as file:
        for l in file:
            keys.append(l)
        return keys


def show_keywords(action, keywords):
    """Show keywords.

    :param action: action from input
    :param keywords: list words
    """
    enter = 1
    allowed_enter = int(len(list(keywords)) / 10)
    rest = int(len(list(keywords)) % 10)

    allowed_enter += 1 if [rest != 0] else allowed_enter

    while action != ' ' and enter <= allowed_enter:
        amount = enter * 10
        init = amount - 10
        if enter == allowed_enter:
            amount = amount - 10 + rest
            init = amount - rest

        for i in range(init, amount):
            print(keywords[i])
        action = read_option()
        enter = enter + 1


def found(url, links):
    """Found url in list links.

    :param url: url
    :param links: list of links
    :return: index
    """
    for l in links:
        if url in str(l):
            return links.index(l) + 1


def check_position(kw):
    """
    Check position if keyword exists into first hundred result.
    :param kw: keyword
    :return: position or code 100
    """
    url = "w3schools.com"

    position = None
    for start in range(0, 100, 10):
        endpoint = f"https://www.google.com/search?q={kw}&start={start}"
        response = requests.get(endpoint)
        soup = BeautifulSoup(response.text, 'lxml')
        links = soup.find_all("div", class_="BNeawe UPmit AP7Wnd")
        position = found(url, links)
        if isinstance(position, int):
            position = start + position
            return position
    if position is None:
        return 100


if __name__ == '__main__':

    keywords = []

    while True:
        value = read_option()
        if value == '1':
            keywords = load_keywords()
        elif value == '2' and len(keywords) != 0:
            show_keywords(value, keywords)
        elif value == '3':
            print('Palabra clave a comprobar: ')
            kw = read_option()
            print(check_position(kw))
        elif value == '0':
            sys.exit()
