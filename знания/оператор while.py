number = 23
running = True
while running:
    guess = int(input('Введите целое число'))

    if guess == number:
        print('Ура, ты угадал!')
        running = False # Это останавливает цикл "while"
    elif guess < number:
        print('Неа, число чуть больше этого')
    else:
        print('Нет, число чуть меньше этого')
else:
    print('Цикл while закончен')
    #здесь можно еще что нибудь выполнить

print('Завершение.')
