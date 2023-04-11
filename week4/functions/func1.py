# найти квадрат,куб, рельтат деления на 100
# num1 = 5
# -> {'2': 25, '3': 125, '100': 0.05}
# num1 = 5
# print({'num': num1, '2': num1 **2, '3': num1 ** 3, '100': num1 / 100})
# num2 = 16
# print({'num': num2, '2': num2 **2, '3': num2 ** 3, '100': num2 / 100})
# num3 = 28
# print({'num': num3, '2': num3 **2, '3': num3 ** 3, '100': num3 / 100})
# num4 = 1154
# print({'num': num4, '2': num4 **2, '3': num4 ** 3, '100': num4 / 100})
# num5 = 31
# print({'num': num5, '2': num5 **2, '3': num5 ** 3, '100': num5 / 100})

# DRY = Don't repeat yourself
# num1 = 5
# num2 = 16
# num3 = 28
# num4 = 1154
# num5 = 31
# def operations(num):
#     print({'num': num, '2': num ** 2, '3': num3** 3, '100': num / 100})
    
# operations(num1)
# operations(num2)
# operations(num3)
# operations(num4)
# operations(num5)
#----------------------------------------------------
# Функция - это именованная часть программы, которая содержит в себе определенный набор инструкций
#и может вызываться в других частях программы столько раз сколько угодно
#--------------------------------------------------------------
# def name_of_function(<a,b>#параметры):
#     <body>#код, какая то логика которая будет давать конечный результат
    #<return> оператор который помогает вернуть результат

# name_of_func(5,6 #аргументы)
#----------------------------------------------------------------------------------------------
# параметры функции это переменные которые будут принимать данные от пользователя и хранить в себе эти данные
# аргументы функции - данные. которые  мы передаем в функцию, в моменте вызова
#------------------------------------------------------------------------------------------------
# ls = [1,2,3,4,5]
# str1 = 'hello world s vami kani i john snow'

# def our_len(obj):
#     i = 0
#     print(obj)
#     for x in obj:
#         i += 1
#     print(f'result: {i}')

# our_len(ls)
# our_len(str1)
#------------------------------------------------------------------------------

# def isEven(obj):
#     # if obj % 2 == 0:
#     #     return True
#     # else:
#     #     return False
#     return True if obj % 2 == 0 else False
    
# print(isEven(5))
# print(isEven(23453422))
# print(isEven(-1))

# def isEven(num: int) -> bool:
#     """Our function returns True or False while checking number for even number
#     """
#     return True if num % 2 == 0 else False

# print(isEven(5))




#-------------------------------------------------------------------------------
# words = ['John', 'ono', 'kaxak', 'peter', 'dodod', 'radar', 'apa', 'piko']
# def get_polindrom(words):
#     result = []
#     for word in words:
#         if word.lower() == word[::-1].lower():
#             result.append(word)
#     return result
    
# polindrom_words = get_polindrom(words)
# print(polindrom_words)
#--------------------------------------------------------------------------------

# def get_percentage(money, period):
#     if money < 30000:
#         raise ValueError('Вложить нужно более 30000!')
#     if period < 3:
#         raise ValueError('минимальный период 3 года!')
#     year = 0
#     while year < period:
#         money += money * 0.1
#         year += 1
#     return money
# try:
#     money = float(input('vvedite summu vlozhenia:'))
#     period = float(input('vvedite period:'))
#     print(get_percentage(money, period))
# except ValueError:
#     print('неправильный ввод!')

# def range(stop, start=0, step=1):
#     pass

# range(5, 2, step=5)
# for i in range(1,22)

#-------------------------------------------------------------------------------------------------------------
