import os, copy

map1 = [["*", "*", "*"], ["*", "G", "*"], ["*", " ", "*"], ["*", " ", "*", "*", "*", "*"], ["*", " ", " ", " ", "K", "*"],
["*", " ", "*", "*", "*", "*"], ["*", " ", "*"], ["*", "D", "*"], ["*", "E", "*"]]

map2 = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
        ['*', 'G', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', 'K', '*'],
        ['*', ' ', '*', '*', '*', '*', '*', ' ', '*', '*', ' ', '*', ' ', '*', '*', '*', ' ', '*', ' ', '*'],
        ['*', ' ', ' ', '*', 'K', '*', '*', 'D', '*', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' ', '*', ' ', '*'],
        ['*', '*', ' ', '*', ' ', ' ', '*', ' ', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', ' ', '*'],
        ['*', ' ', ' ', '*', '*', ' ', '*', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
        ['*', ' ', '*', '*', ' ', ' ', '*', '*', ' ', '*', '*', '*', ' ', '*', '*', 'D', '*', ' ', '*', '*'],
        ['*', ' ', '*', ' ', ' ', '*', '*', '*', ' ', ' ', ' ', '*', ' ', '*', 'K', ' ', '*', ' ', '*', '*'],
        ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', ' ', '*', ' ', '*', '*', '*', ' ', ' ', '*', '*'],
        ['*', ' ', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', ' ', '*', '*', ' ', ' ', '*', 'K', '*'],
        ['*', ' ', '*', 'K', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', '*', ' ', '*', '*', ' ', '*'],
        ['*', ' ', ' ', ' ', '*', ' ', '*', '*', '*', 'D', '*', '*', '*', '*', '*', ' ', '*', ' ', ' ', '*'],
        ['*', '*', '*', 'D', '*', ' ', '*', 'K', '*', ' ', ' ', ' ', ' ', ' ', '*', ' ', '*', '*', ' ', '*'],
        ['*', ' ', '*', ' ', '*', ' ', '*', ' ', '*', ' ', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
        ['*', ' ', ' ', ' ', ' ', ' ', '*', ' ', '*', ' ', '*', '*', '*', ' ', '*', '*', '*', '*', ' ', '*'],
        ['*', '*', ' ', '*', '*', '*', '*', ' ', '*', ' ', '*', ' ', '*', ' ', ' ', ' ', ' ', '*', ' ', '*'],
        ['*', ' ', ' ', '*', ' ', ' ', '*', ' ', '*', ' ', '*', ' ', '*', ' ', ' ', ' ', ' ', '*', ' ', '*'],
        ['*', ' ', '*', '*', '*', ' ', '*', ' ', '*', ' ', '*', ' ', '*', ' ', '*', ' ', '*', '*', '*', '*'],
        ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
        ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', 'E', '*']]

map_test = [['*', '*', '*', '*', '*'], ['*', 'D', 'K', ' ', '*'], ['*', ' ', 'G', ' ', '*'], ['*', ' ', ' ', ' ', '*'],
['*', 'E', '*', '*', '*'],]

pamitka = '''Цель игры дойти до выхода и выжить
Управление:           Легенда карты: 
    W - вверх,            G - главный герой,
    A - влево,            K - ключ,
    S - вниз,             D - дверь,
    D - вправо,           E - выход
    H - помощь
    Q - выход в меню'''

pamitka_menu = 'Управление: w - вверх,  s - вниз, e - выбор'

menu_txt = """ ██╗ ███╗  ██╗ ███████╗  █████╗          ██████╗  █████╗  ███╗   ███╗ ███████╗
 ██║ ████╗ ██║ ██╔════╝ ██╔══██╗       ██╔════╝  ██╔══██╗ ████╗ ████║ ██╔════╝
 ██║ ██╔██╗██║ █████╗   ██║  ██║       ██║  ██╗  ███████║ ██╔████╔██║ █████╗
 ██║ ██║╚████║ ██╔══╝   ██║  ██║       ██║  ╚██╗ ██╔══██║ ██║╚██╔╝██║ ██╔══╝
 ██║ ██║ ╚███║ ██║      ╚█████╔╝       ╚██████╔╝ ██║  ██║ ██║ ╚═╝ ██║ ███████╗
 ╚═╝ ╚═╝  ╚══╝ ╚═╝       ╚════╝         ╚═════╝  ╚═╝  ╚═╝ ╚═╝     ╚═╝ ╚══════╝"""

menu_yacheiki = ['1. Играть', '2. Настройки', '3. Выход']

version = 'pre_alfa_test 1.0v New: -'


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


all_maps = [Maping('Тестовая карта', map_test, 2, 2), Maping('Уровень 1', map1, 1, 1), Maping('Уровень 2', map2, 1, 1)]


def vivod_menu(yacheika, yvedomlenie=[], vivod_chego=0):
    os.system('cls')
    print(menu_txt, '\n', version)
    print(pamitka_menu)
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
        all_maps.append('Назад в меню')
        for i in all_maps:
            if chet == yacheika:
                if i == 'Назад в меню':
                    print(f'{chet + 1}. {i} <')
                else:
                    print(f'{chet + 1}. {i.name} <')
            else:
                if i == 'Назад в меню':
                    print(f'{chet + 1}. {i}')
                else:
                    print(f'{chet + 1}. {i.name}')
            chet += 1
        all_maps.pop()


def menu():
    yvedomlenie = []
    yacheika = 0
    menu_maps = 0
    vivod_menu(yacheika, yvedomlenie)
    while True:
        destvia = input().lower()
        if destvia == 'w' or destvia == 'ц':
            yacheika -= 1
            if yacheika < 0:
                yacheika = len(all_maps)
        elif destvia == 's' or destvia == 'ы':
            yacheika += 1
            if yacheika > len(all_maps):
                yacheika = 0
        else:
            if menu_maps == 0:
                if yacheika == 0:
                    menu_maps = 1
                    yacheika = 0
                elif yacheika == 1:
                    yvedomlenie.append(['Скоро появится', 3])
                else:
                    break
            elif menu_maps == 1:
                if yacheika == len(all_maps):
                    menu_maps = 0
                    yacheika = 0
                else:
                    map_play(all_maps[yacheika])

        vivod_menu(yacheika, yvedomlenie, menu_maps)


def vivod_map(maps, yvedomlenie=[]):
    os.system('cls')

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
    yvedomlenie = [[pamitka, 3]]
    vivod_map(map.map, yvedomlenie)
    map_cash = copy.deepcopy(map.map)
    kluch_cash = copy.deepcopy(map.kluch)

    while True:
        destvia = input().lower()
        new_x, new_y = x, y

        if destvia == 'd':
            new_x += 1
        elif destvia == 'a':
            new_x -= 1
        elif destvia == 'w':
            new_y -= 1
        elif destvia == 's':
            new_y +=  1
        elif destvia == 'h':
            yvedomlenie = [[pamitka, 3]]
        elif destvia == 'q':
            break
        else:
            yvedomlenie.append([f'Нет такого действия: {destvia}', 2])

        if map_cash[new_y][new_x] == ' ': # emptiness
            map_cash[new_y][new_x] = 'G'
            map_cash[y][x] = ' '
            x, y = new_x, new_y
        elif map_cash[new_y][new_x] == 'D': # door
            if kluch_cash > 0:
                map_cash[new_y][new_x] = 'G'
                map_cash[y][x] = ' '
                x, y = new_x, new_y
                yvedomlenie.append(['Вы открыли дверь', 3])
                kluch_cash -= 1
            elif kluch_cash == 0:
                yvedomlenie.append(['Чтобы открыть дверь надо подобрать ключ', 3])
        elif map_cash[new_y][new_x] == 'K' or map.map[new_y][new_x] == 'К': # key
            map_cash[new_y][new_x] = 'G'
            map_cash[y][x] = ' '
            x, y = new_x, new_y
            kluch_cash += 1
            yvedomlenie.append(['Вы подобрали ключ!', 3])
        elif map_cash[new_y][new_x] == 'E': # exit
            os.system('cls')
            break
        elif map_cash[new_y][new_x] == '*': # wall
            yvedomlenie.append(['Вы уперлись в стену!', 3])

        vivod_map(map_cash, yvedomlenie)

menu()