import os

map1 = [
    ["*", "*", "*"],
    ["*", "G", "*"],
    ["*", " ", "*"],
    ["*", " ", "*", "*", "*", "*"],
    ["*", " ", " ", " ", "K", "*"],
    ["*", " ", "*", "*", "*", "*"],
    ["*", " ", "*"],
    ["*", "D", "*"],
    ["*", "E", "*"]]

map_test = [
    ['*', '*', '*', '*', '*'],
    ['*', 'D', 'K', ' ', '*'],
    ['*', ' ', 'G', ' ', '*'],
    ['*', ' ', ' ', ' ', '*'],
    ['*', 'E', '*', '*', '*'],]

pamitka = '''Цель игры дойти до выхода и выжить
Управление:           Легенда карты: 
    W - вверх,            G - главный герой,
    A - влево,            K - ключ,
    S - вниз,             D - дверь,
    D - вправо,           E - выход
    H - помощь'''

pamitka_menu = 'Управление: w - вверх,  s - вниз, e - выбор'

version = 'alfa 1.0v'

menu_txt = """ ██╗ ███╗  ██╗ ███████╗  █████╗          ██████╗  █████╗  ███╗   ███╗ ███████╗
 ██║ ████╗ ██║ ██╔════╝ ██╔══██╗       ██╔════╝  ██╔══██╗ ████╗ ████║ ██╔════╝
 ██║ ██╔██╗██║ █████╗   ██║  ██║       ██║  ██╗  ███████║ ██╔████╔██║ █████╗
 ██║ ██║╚████║ ██╔══╝   ██║  ██║       ██║  ╚██╗ ██╔══██║ ██║╚██╔╝██║ ██╔══╝
 ██║ ██║ ╚███║ ██║      ╚█████╔╝       ╚██████╔╝ ██║  ██║ ██║ ╚═╝ ██║ ███████╗
 ╚═╝ ╚═╝  ╚══╝ ╚═╝       ╚════╝         ╚═════╝  ╚═╝  ╚═╝ ╚═╝     ╚═╝ ╚══════╝"""

menu_yacheiki = ['1. Играть', '2. Настройки', '3. Выход']



class Essence:
    def __init__(self, hp, attack):
        self.hp = hp
        self.attack = attack
        self.inventory = {}



class Maping:
    def __init__(self, name, map, x, y):
        self.name = name
        self.map = map
        self.x = x
        self.y = y
        self.kluch = 0



all_maps = [Maping('Тестовая карта', map_test, 2, 2), Maping('Уровень 1', map1, 1, 1), Maping('Назад в меню', 0, 0, 0)]


def vivod_menu(yacheika, yvedomlenie=[], vivod_chego=0):
    os.system('cls')
    print(menu_txt, '\n', version)
    print(pamitka_menu)
    print()
    chet = 0
    if len(yvedomlenie) != 0:
        new_yvedomlenie = []
        for i in yvedomlenie:
            if i[1] > 0:
                i[1] -= 1
                print(i[0], end='\n')
                new_yvedomlenie.append(i)
        yvedomlenie = new_yvedomlenie

    if vivod_chego == 0:
        for i in menu_yacheiki:
            if chet == yacheika:
                print(f'{i} <')
            else:
                print(i)
            chet += 1
    elif vivod_chego == 1:
        for i in all_maps:
            if chet == yacheika:
                print(f'{i.name} <')
            else:
                print(i.name)
            chet += 1


def menu():
    yvedomlenie = []
    yacheika = 0
    vivod_menu(yacheika, yvedomlenie)
    while True:
        destvia = input().lower()
        if destvia == 'w':
            yacheika -= 1
            if yacheika < 0:
                yacheika = len(all_maps) - 1
        elif destvia == 's':
            yacheika += 1
            if yacheika > len(all_maps) - 1:
                yacheika = 0
        else:
            if yacheika == 0:
                yacheika = 0
            elif yacheika == 1:
                yvedomlenie.append(['Скоро появится', 3])
            else:
                break

        vivod_menu(yacheika, yvedomlenie)


def menu_yrav():
    yvedomlenie = []
    yacheika = 0
    vivod_menu(yacheika, yvedomlenie, 1)
    while True:
        destvia = input().lower()
        if destvia == 'w':
            yacheika -= 1
            if yacheika < 0:
                yacheika = len(menu_yacheiki) - 1
        elif destvia == 's':
            yacheika += 1
            if yacheika > len(menu_yacheiki) - 1:
                yacheika = 0
        else:
            if yacheika == 0:
                yacheika = 0
            else:
                menu()
    vivod_menu(yacheika, yvedomlenie, 1)


def vivod_map(pamitkas, maps, yvedomlenie=[]):
    os.system('cls')
    if pamitkas:
        print(pamitka, end='\n')

    if len(yvedomlenie) != 0:
        new_yvedomlenie = []
        for i in yvedomlenie:
            if i[1] > 0:
                i[1] -= 1
                print(i[0], end='\n')
                new_yvedomlenie.append(i)
        yvedomlenie = new_yvedomlenie

    for i in maps:
        for x in i:
            print(x, end='')
        print(end='\n')


def map_play(map):
    x, y = map.x, map.y
    vivod_map(1, map.map)
    yvedomlenie = []

    while True:
        destvia = input().lower()
        star_x, star_y = x, y
        pamitkas = 0

        if destvia == 'd':
            x += 1
        elif destvia == 'a':
            x -= 1
        elif destvia == 'w':
            y -= 1
        elif destvia == 's':
            y +=  1
        elif destvia == 'h':
            pamitkas = 1

        if map.map[y][x] == ' ':
            map.map[y][x] = 'G'
            map.map[star_y][star_x] = ' '
        elif map.map[y][x] == 'D':
            if map.kluch == 1:
                map.map[y][x] = 'G'
                map.map[star_y][star_x] = ' '
                yvedomlenie.append(['Вы открыли дверь', 3])
            elif map.kluch == 0:
                yvedomlenie.append(['Чтобы открыть дверь надо подобрать ключ', 3])
        elif map.map[y][x] == 'K' or map.map[y][x] == 'К':
            map.map[y][x] = 'G'
            map.map[star_y][star_x] = ' '
            map.kluch = 1
            yvedomlenie.append(['Вы подобрали ключ!', 3])
        elif map.map[y][x] == 'E':
            os.system('cls')
            print('You win!')
            break
        elif map.map[y][x] == '*':
            x, y = star_x, star_y
        else:
            yvedomlenie.append([f'Нет такого действия: {destvia}', 2])
            x, y = star_x, star_y

        vivod_map(pamitkas, map.map, yvedomlenie)


menu()
