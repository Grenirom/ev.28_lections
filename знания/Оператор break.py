while True:
    s = input('Введите что-нибудь : ')
    if s == 'выход':
        break
    if len(s) < 3:
        print('Слишком мало')
        continue
    print('Введеная строка достаточной длины')
#Заметьте, что оператор continue также работает и с циклом for

