# calculator v1
what = input( ' выберите действие: ( +, -, *, /) ' )

a = float (input(' Введите первое число: '))
b = float (input( ' введи второе число: '))

if what == '+':
    v = a + b
    print( ' Результат: ' + str(v) )

elif what == '*':
    v = a * b
    print('Результат:' + str(v) )
elif what == '/':
    v = a / b
    print(' Результат: ' + str(v) )
elif what == '-':
    v = a - b
    print('Результат:' + str(v))

else:
    print("Выбрана неверная операция!")