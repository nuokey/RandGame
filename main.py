import random
from time import sleep
print('''
 ____   ____          ____   ____
|    | |    | |\   | |    \ |    | |\  /|
|____| |____| | \  | |    | |    | | \/ |
|   |  |    | |  \ | |    | |    | |    |
|   |  |    | |   \| |____/ |____| |    |
''')
kub = ['''
 _____
|     |
|  .  |
|_____|
'''], ['''
 _____
|     |
| . . |
|_____|
'''], ['''
 _____
|  .  |
| . . |
|_____|
'''], ['''
 _____
| . . |
| . . |
|_____|
'''], ['''
 _____
| . . |
|. . .|
|_____|
'''], ['''
 _____
|. . .|
|. . .|
|_____|
''']
sleep(1)
vig = 0
br = 0
c = open("chance.txt")
l = open("level.txt")
o = open("money.txt")
chance = int(c.read())
level = int(l.read())
money = int(o.read())
while True:
    print('Ваш шанс:',chance)
    print('Ваш уровень:', level)
    print('Ваши очки:', money)
    print('Общие шансы: ', chance, '/', level * 5, sep='')
    print()
    print('0. Random')
    print('1. Игра')
    print('2. Поднять уровень(+75)')
    print('3. Улучшить шанс(-50, +шанс)')
    print('4. Игра на ставки')
    print('5. ClickGame')
    print('6. Кубики')
    a = input()
    if a == '1':
        ch = random.randint(0, level * 7)
        for i in range(0, chance):
            if ch == i:
                money += level * 5
                print('Вы получили', level * 5)
                print()
                vig = 1
        if vig != 1:
            print('Вы ничего не получили')
        else:
            vig = 0
        sleep(1)
    if a == '2':
        level += 1
        money += 75
    if a == '3':
        if money >= 50:
            money -= 50
            chance += 1
    c = open("chance.txt","w")
    l = open("level.txt", "w")
    o = open("money.txt","w")
    c.write(str(chance))
    l.write(str(level))
    o.write(str(money))
    c.close()
    l.close()
    o.close()
    if a == '4':
        if level >= 5:
            st = int(input('Введите ставку'))
            if st > money:
                st = 0
                print('Ставка обнуляется')
            money -= st
            vi = random.randint(0, 100)
            for n in range(0, 40):
                if n == vi:
                    money += 2 * st
                    print('Вы выйграли')
                    br = 1
            if br != 1:
                print('Вы проиграли')
            if br == 1:
                br = 0
        else:
            print('У вас недостаточный уровень!')
        print('')
    if a == '5':
        ch = input()
        money += len(ch)
        print('Вы набрали', len(ch))
        print('')
        open("money.txt", "w")
        m = open("money.txt", "w")
        m.write(str(money))
        m.close()
    if a == '0':
        mini = int(input('Введите первое число '))
        maxi = int(input('Введите второе число '))
        print('')
        print('Выпало', random.randint(mini, maxi))
        print('')
    if a == '6':
        kubk = int(input('Введите кол-во кубиков '))
        for ku in range(kubk):
            print(ku + 1,'кубик -', random.randint(0, 5))
        print('')
