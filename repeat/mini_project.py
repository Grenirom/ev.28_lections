#-------------------------------------------------------
#       УГАДАЙ ЧИСЛО

from random import randint
name = input('Здравствуй! Введи свое имя:')
choice = input(f'{name} ты хочешь играть?(yes/no):')
rand = randint(1,10)
i = 3
tries = 0

while i > 0:
    if choice.lower().strip() == 'yes':
        print('Приступим!')
    else:
        print('Хорошо, пока!')
        break
    
    print(rand)
    numg = int(input('Введи загаданное число(в диапозоне от 1 до 10):'))
    print()
    if numg == rand:
        tries += 1
        print(f'Ты угадал, с {tries} попытки!')
        choice = input('ты хочешь продолжить игру?(yes/no):')
        if choice.strip().lower() == 'yes':
            tries = 0
            rand = randint(1,10)
            i = 3
            print()
        else:
            print('Пока!')
            break
    else:
        i -= 1
        tries += 1
        print(f'Ты не угадал, у тебя осталось {i} попытки!')
        if i == 0 and tries == 3:
            print(f'Загаданое число -- {rand}')
#если что то упустил, прошу понять и простить