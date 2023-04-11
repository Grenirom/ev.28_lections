# оепраторы сравнения 
# условные операторы
# логические операторы
#операторф сравнения
# <, >, ==(равно), !=(не равно), <=, >=

#1 < 5 = true
# 7 > 9 = False
# ord('') - проверить ascii код
#chr(320) - проверить букву под цифрой 

# Условные операторы
# if
# elif
# else
# if <condition>:
#     <body if> #сработает если в condition выведет True
#[elif] <condition>:
#     <body elif>
# [else]:
#     <body else> # сработает если во всех вышестощих условиях пришло False

# string = input('enter smth:')

# if string.lower() == 'hello':
#     print('Hello, it\'s me, i was womdering if after all these years you\'d like to meet')
# elif string.lower() == 'john':
#     print('Welcome back John Snow, the king of north')
# elif string.lower() == 'abra-kadabra':
#     print('sim salamon')
# else:
#     print('совпадений не найдено')
# print('registration form:')
# email = input('Enter your email:')
# password = input('Enter the password:')
# if len(password) < 8:
#     raise ValueError('Password is too short!\n Gotta be 8 symbols or more!') # вытаскивает ошибку принудительно, и останавливает код
#     # print('password too short')
# elif password.isdigit():
#     raise ValueError('Password must contain symbolls too!')
# elif password.isalpha():
#     raise ValueError('Password must contain numbers or special symbols too!')

# print('OK!')
# password2 = input('Enter password confirmation:')
# if password == password2:
#     print('you\'re allowed to enter')
# else:
#     raise ValueError('passwords did not match!')

# print(f'You\'re succesfully registered mr/mrs {email}')

# age = input('Введите ваш возраст:')
# if age.isdigit():
#     age = int(age)
# else:
#     raise Exception('Invalid value for age!')

# if age < 18:
#     print(f'Access Denied! Come again in {18 - age} years!')
# else:
#     print('you can pass! welcome to the US!')

# and - логическое и
# or - логическое или
# not - логическое отрицание

# money = 1_000_001
# status = 'premium'

# if money > 1_000_000 and status == 'premium':   #чтобы вернуть True, 2 условия должны быть выполнены
#     print('You\'re the president of our club!')
# elif money > 1_000_000 or status == 'premium':     #здесь должно выполниться хотя бы одно условие чтобы выдать true
#     print('You\'re the minister of our club')
# else:
#     print('You\'re honorable member of our club')

# str1 = 'Hello World!'
# print(str1)
# symbol = input('Enter the symbol:')

# # if symbol not in str1:
# #     print(f'the symbol: {symbol} does not exist')
# # else:
# #     print(f'The symbol: {symbol} exists!')


# if symbol in str1:
#      print(f'the symbol: {symbol} exists')
# else:
#      print(f'The symbol: {symbol} does not exist!')

# Разрешаем доступ если он пользователь гита или гугла и его возраст больше 21 или у него есть деньги (10000)

# user = 'John'
# is_goggle_user = True
# is_git_user = False
# age = 20
# user_coins = 9000
# if (is_git_user or is_goggle_user) and (age > 21 or user_coins > 10000):
#     print(f'You can enter the system mr/mrs {user}!')
# else:
#     print('Sorry, you\'re not allowed to the system!')

#                    ЗАДАНИЕ № 8
#В переменные x, y попадают числа вводимые пользователем. 
# Проверить делится ли первое число на второе без остатка.
# Программа должна вывести на экран следующую информацию:
# частное - выводить в любом случае
# если число делится с остатком, вывести остаток от деления
# x = int(input('Введите первое число:'))
# y = int(input('Введите второе число:'))

# if x / y and x % y == 0:
#     print(f'x делится на y')
#     dev = x // y
#     print(f'Частное: {dev}')
# else:
#     res = x // y
#     print('x не делится на y')
#     print(f'Частное: {res}')
#     dev = x % y
#     print(f'Остаток: {dev}')



#               ЗАДАНИЕ№9
# В переменную year попадает число-год от пользователя.
# Определите, является ли год с данным номером високосным.
# Если год является високосным, то выведите YES, иначе выведите NO.
# Note: в соответствии с григорианским календарем, год является високосным в двух случаях: 
# 1) если число года делится без остатка на 4 и НЕделится на 100,
# 2) либо число года делится без остатка на 400.

#                 РЕШЕНИЕ:
# year = int(input('Введите год:'))

# if (year / 4 and year % 4 == 0) and (year % 100 != 0):
#     print('YES')

# elif year / 400 and year % 400 == 0:
#     print('YES')
# else:
#     print('NO')


# string = 'hello my name is nick'
# print(string[1::2])
# nums = [4,11,2,5,1,6]
# target = 8
# for i in range(0, len(nums)):
#     print(i)
#     print(nums[i])
# a = input()
# b = input()
# c = input()
# sort_ = [a, b, c]
# print(sort_.sort)



month = int(input('введите номер  месяца'))
if month > 12:
    print('Такого месяца нет')
elif month == 1 and month == 2 and month == 12:
    print('зима')
elif month == 3 and month == 4 and month == 5:
    print('весна')
elif month == 6 and month == 7 and month == 8:
    print('лето')
elif month == 9 and month == 10 and month == 11:
    print('осень')



