'string' 

'''
hello wrld
'''
"""
hello
my name is
"""

#Строки - набор последовательных символов которые мы используем
#для хранения и представления текстовой информации

#Индексация в строке 
# name = "John"       #Индекс начинается с нуля
        # j = 0 = -4
        # 0 = 1 = -3
        # h = 2 = -2 
        # n = 3 = -1
# print(name)
# print(name[1])  #чтобы обратиться по индексу, в обратную сторону индексация идет с (-1),
# #обязательно индекс нужно взять в квадратные скобки
# print('kani'[-1],"kani"[2])
# str1 = "kani"
# print(str1 [1], str1 [3])

# str1 = 'birthday'
# print(str1[4], str1[6], str1[7])
# print(str1[0], str1[1], str1[2], str1[3], str1[4])

# print(str1[0] + str1[1] + str1[2] + str1[3] + str1[4])  # + - используется для соединения строк

#Срезы по индексам
#[start: end: <step>]
# str1 = 'birthday'
# print(str1[5:8]) #указывая конечный индекс к примеру число 7, само число 7 не включается в строку
#                 #но чтобы получить слово до конца можно после первого числа и двоеточия ничего не указывать
# print(str1[:6])
# print(str1[5:])

# text = 'hello world! my name\'s nick'    #'i\'m' - экранирование

# print(text [:13])
# print(text[::2]) #:: - показывать текст через шаг, после первого мы берем каждый второй символ 
# # пробел идет в символ
# text = 'hello'
# print(text[::-1]) #вывести строку с конца, используется индекс [-1]

# Конкатенация строк(соединение)

# a = 'hello'
# b = 'world'
# c = ' '
# print(a + c + b)

# Экранирования - способ записи символов в строку, которые невозможно ввести
# с клавиатуры

#\n -> перенос строки
# \t -> горизонтальная табуляция
# \v -> вертикальная табуляция
# \f -> перевод страницы
# \r -> возврат указателя
# print('hello world!\nMy name is Nick')
# print('hello world!\tMy name is Nick')
# print('hello world!\vMy name is Nick')
# print('hello world!\fMy name is Nick')
# print('hello world!\rMy name is Nick')


# Форматирования строк - изменение вида строки из одного в другую
# 1) С помощью знака %
# 2) С использованием .format()
# 3) Интерполяция строк

#%
# name = input('Введите имя:')
# last_name = input('Введите свою фамилию:')
# #print('Добро пожаловать к нам, ' + name + ' ' + last_name + '!')
# print('Hello mr/mrs %s %s!' %(name, last_name))  #s возле процента это str (строка)

# .format
# name = input('Введите имя:')
# last_name = input('Введите свою фамилию:')
# print('Приветствую вас, {} {}, в наш дом!'.format (name, last_name))
 #{} {} - это информация которую далее при помощи .format(..... , .....)
# # мы указываем в самих {}


# Интерполяция - преобразование строки (f-stroki)
# a = input('Enter mrs/mr:')
# name = input('Введите имя:')
# last_name = input('Введите свою фамилию:')
# print(f'Hello {a} {name} {last_name}! Welcome to the party!')


# text = 'Запомни Питер, с большой силой приходит и большая ответственность.'
# reversed_text = text[::-1]
# # print(reversed_text)
# i = 0
# count_t = 0 
# len_text = len(reversed_text)
# #print(len(reversed_text)) # len - выводит количество символов нашей строки
# while i <len_text:
#     symbol = reversed_text[i]
#     if symbol == 'т' or symbol == 'Т': # Т == т - false
#         count_t += 1
#     print(reversed_text[i])
#     i += 1 # Инкремент i = i + 1

# print(f'В тексте буква "т" встретилась {count_t} раз!')

string = 'hello' 
print (string[-1] + string[1:-1] +string[0])














