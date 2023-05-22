# str
# ''
# 'hello'
# str(5)

# print(dir(str))
# print(dir(int))

# a = 'hello'
# b = 'nick'
# print(a != b)    #!= - знак неравенства
# print('abc' == 'abc')
# print(a > b)
# print(a < b)
# print('a') # 97 -> 1100001
# print('a' > 'b') #97>98
# print('h'> 'c') #104 > 99

# print('hello' > 'harry') #true
# print('abc' > 'abc') #false

#len - возвращает количесво символов в строке
# a = 'Hello'
# b = 'johnsnow'
# print(len(a) < len(b))  # True
# print(len(a))
# print(len(b))

# <, >, ==, !=, >=, <=

# методы строк - принимает в себя старое значение новое значение и count
# replace(old, new, [count]) - меняет в строке символы old на new, 
#если вы укажете count, то заменит count раз


# text = 'ha ha ha ha' # метод используется только с строками
# result = text.replace('a', 'e', 2) # a - старый символ, меняет на символ e, 2 - количество замен
# print(text)
# print(f'result after replace: {result}')

# str1 = 'helloWorld
#my name is johnsnow'
# result = str1.replace('johnsnow', 'jamieLanister') # Указываем имя переменной, потом . , потом сам метод replace
# print(result)

# strip() - Убирает пробельные символы в начале и в конце строки
# есть методы rstrip, lstrip
# #lstrip - удаление пробелов слева
#rstrip - Удаление пробелов справа
# a = '   He l lo   '
# print(len(a))
# print(a)
# res = a.strip()
# print(res)
# print(len(res))
# print(dir(str))

# isdigit -                        Проверяют
# isnumeric -                состоит ли наша строка
# isdecimal -                    полностью из чисел

# num = input('Введите число:')
# print(f'Введено число?: {num.isdigit()}')

# num = input('Введите число:')
# if num.isdigit():
#      num = int(num)
#      print(f'{num} + 5 = {num + 5}')
# else:
#     print('Вы ввели не числа!')

# text = '\u0031'
# print(text)
# print(text.isnumeric())
# print(text.isdigit())
# print(text.isdecimal())

# # isalnum() -> Проверяет состоит ли наша строка из чисел и символов латинского и киррилицы алфавита
# str1 = '56a'
# print(str1.isalnum())
# str2 = '56_a'  #false при спец символах (-, _ и тд.)
# print(str2.isalnum())

#isalpha() - состоит ли наша строка полностью из символов алфавита 
# str1 = 'asdaajk sf!'
# res = str1.replace(' ', '')
# print(res)
# print(res.isalpha())   # Спец символы не принимает

#islower() - проверяет, состоит ли строка из только символов нижнего регистра
# isupper() - проверяет, состоит ли строка из только символов верхнего регистра
# istitle() - проверяет, начинается ли строка с символа верхнего регистра
# str1 = 'Ms. My Name'
# print(str1.islower()) #False
# str2 = 'FUSFBS BEFH'
# print(str2.isupper()) #False
# print(str1.istitle()) #True

# index(value, [start], [end]) - выводит индекс значения value,   # все что находится в квадратных скобках - опционально
# которое мы передаем в нашей строке
# text = 'Hello john snow'
# print(text.index('john', 2, 10)) 
# text = 'Hello world! my name is john snow!'
#print(text.index('o'))
# res = text.index('o')
# print(res) #4
# res = text.index('o', res + 1)# 7
# print(res)
# res = text.index('o', res + 1)# 25
# print(res)
# res = text.index('o', res + 1)#31
# print(res)

# count(value, [start]) - считает количество вхождений value в нашу строку 
# text = 'hello o o o hello'
# res = text.count('l')
# print(res)

#split(separator) - Дробит нашу строку на несколько частей по разделителю
#все части строк сохраняются в типе данных list
# text = 'helloworld my namedf no namy by name of myself'
# res = text.split(' ')
# print(res)
# print(len(res))

# a = '#hello#hello#hello#hello#hello'
# res = a[1].split('#')
# print(res)

# 'connector'.join(list) -> соединяет по connector строки которые находились в list
text = 'helloworld my namedf no namy by name of myself'
res = text.split(' ')
print(res)
# str1 = ' '.join(res)
# print(str1)

#find(value, [start], [end]) - ДЕлает тоже самое что и index, но если не нашел то вернется -1
# text = 'hello'
# print(text.find('joji'), type(text.find('joji')))
# print(text.index('joji'))
# print('hello')
# swapcase() - переводит все символы в противоположный регистр
# upper() - переводит вс

# swapcase() - переводит все символы в противоположный регистр
# upper() - переводит все в верхний регистр
# lower() - переводит все в нижний регистр
# text = 'hellkSHX1123o'
# print(f'original: {text}')
# print(text.upper())
# print(text.lower())
# print(text.swapcase())

#capitalize() - переводит самый первый символ в верхний регистр
#title() - переводит первые символы всех слов в верхний регистр
# text = input('Введите ваше имя:').capitalize()
# print(text)
# print(text.title())

# fio = 'jOJI kIPNIN kOPKP'
# print(fio.title())
# print(dir(str))


# print((1, 'a') > ('b', 2))
# print((1,-1,0) > (1,1))
# print(dir(str))