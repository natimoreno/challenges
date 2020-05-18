import sys

print('[1] - Importar palabras clave')
print('[2] - Mostrar palabras clave')
print('[0] - Salir')


def load_keywords():
    keys = []
    with open('keywords.txt', 'r') as file:
        for l in file:
            keys.append(l)
        return keys


def read_option():
    return input()


if __name__ == '__main__':

    keywords = []
    value = read_option()

    if value == '1':
        keywords = load_keywords()
        value = read_option()

    if value == '2' and len(keywords) != 0:
        enter = 1
        allowed_enter = int(len(list(keywords)) / 10)
        rest = int(len(list(keywords)) % 10)

        allowed_enter += 1 if [rest != 0] else allowed_enter

        while value != ' ' and enter <= allowed_enter:
            amount = enter * 10
            init = amount - 10
            if enter == allowed_enter:
                amount = amount - 10 + rest
                init = amount - rest

            for i in range(init, amount):
                print(keywords[i])
            value = read_option()
            enter = enter + 1

    if value == '0':
        sys.exit()
