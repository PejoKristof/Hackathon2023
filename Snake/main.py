from random import randint

def print_field():
    for x in cellak:
        if x in snake_body:
            print('@', end='')
        elif x[1] in (0, palya_magassag - 1) or x[0] in (0, palya_szelesseg - 1):
            print('*', end='')
        else:
            print(' ', end='')
        if x[0] == palya_szelesseg - 1:
            print('')

def update_snake():
    new_head = snake_body[0][0] + direction[0], snake_body[0][1] + direction[1]
    snake_body.insert(0,new_head)

palya_szelesseg = 60
palya_magassag = 30
cellak = [(col, row) for row in range(palya_magassag) for col in range(palya_szelesseg)]

snake_body = [(randint(1,50), palya_magassag // randint(2,5))]
DIRECTIONS = {'balra': (-1, 0), 'jobbra': (1, 0), 'fel': (0, -1), 'le': (0, 1)}
direction = DIRECTIONS['jobbra']

while True:
    print_field()

    bekert = input("Hova? ")
    if bekert == "balra" :
        direction = DIRECTIONS['balra']
    elif bekert == "jobbra" :
        direction = DIRECTIONS['jobbra']
    elif bekert == "fel" :
        direction = DIRECTIONS['fel']
    elif bekert == "le" :
        direction = DIRECTIONS['le']
    elif bekert == "meguntam" :
        print("Most ennyi volt, szép napot!")
        break

    update_snake()

    if snake_body[0][1] in (0, palya_magassag - 1) or \
            snake_body[0][0] in (0, palya_szelesseg - 1) or \
            snake_body[0] in snake_body[1:]:
        bekert = input("Hova? ")
        if bekert == "balra":
            direction = DIRECTIONS['balra']
        elif bekert == "jobbra":
            direction = DIRECTIONS['jobbra']
        elif bekert == "fel":
            direction = DIRECTIONS['fel']
        elif bekert == "le":
            direction = DIRECTIONS['le']
        elif bekert == "meguntam":
            print("Most ennyi volt, szép napot!")
            break