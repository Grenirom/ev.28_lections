number = 43
guess = int(input('Введите целое число : '))
if guess == number:
    print('Вы угадали число!')
elif guess < number:
    print('Загаданное число чуть больше этого!')

elif guess > number:
    print('Загаданное число чуть меньше этого!')
else:
    print('Неа!')
print('Завершено')
