import random


# функция определения урона
def damage_done():
    return random.randint(5, 20)


# функция нанесенного урона и оставшегося здоровья
def attack(person1, person2):
    damage_person = round(damage_done() / person2['armor'], 1)
    person1['health'] = round(person1['health'] - damage_person, 1)
    print('{} нанес урон {}, здоровье {} - {}'.format(person2['name'], damage_person, person1['name'],
                                                      person1['health']))


# function creation person
def define_player(name, health=100, armor=1.2):
    print(name, health, armor)
    return {'name': name, 'health': health, 'armor': armor}


# function to write structure to file
def write_player_to_file(person):
    with open('D:\\Python projects\\Battle_two_persons\\' + person['name'] + '.txt', 'w', encoding='UTF-8') as f:
        # with open(person['name'], 'w', encoding='UTF-8') as f:
        for k, v in person.items():
            f.write('{} {}\n'.format(k, v))


# функция для получения структуры из файла
def player_by_filename(name):
    player = {}
    file = 'D:\\Python projects\\Battle_two_persons\\' + name + '.txt'  # str(filename)
    with open(file, encoding='UTF-8') as f:
        for line in f:
            k, v = line.split()
            if k == 'health':
                v = int(v)
            elif k == 'armor':
                v = float(v)
            player[k] = v
    print(player)
    return player


# функция старта игры
def start_game():
    hero = player_by_filename(name1)
    enemy = player_by_filename(name2)
    while True:
        if hero['health'] > 0 and enemy['health'] > 0:
            attack(hero, enemy)
        if enemy['health'] > 0 and hero['health'] > 0:
            attack(enemy, hero)
        else:
            break

    if hero['health'] <= 0:
        print('Enemy WIN!')
    else:
        print('Hero WIN!')


# HERO = {'name': 'hero', 'health': 100, 'armor': 1.3}
# ENEMY = {'name': 'enemy', 'health': 100, 'armor': 1.2}

# присвоение имен
name1 = 'Hero'
name2 = 'Enemy'

# вызов функции создания словаря персонажа
player1_dict = define_player(name1)
player2_dict = define_player(name2)

# вызов функции для записи словаря в файл
write_player_to_file(player1_dict)
write_player_to_file(player2_dict)

start_game()
