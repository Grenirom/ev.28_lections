# list() -- (списки, массив) - изменяемый последовательный тип данных
# который представляет из себя колекцию каких либо обьектов (значения)

# my_list = [1, 'string', False, None, [1,2,3,4]] # может включать в себя все типы данных
# print(my_list, type(my_list))

# range() - возвращает последовательность элементов (чисел)
# ls = range(1, 101)
# my_list = list(ls)
# print(my_list)

# list()
# my_list = list('hello world') #раздробтлт текст по буквам
# print(my_list)

# tuple_ = ('banana', 'apple', 'cherry')
# print(tuple_, type(tuple_))
# ls = list(tuple_)
# print(ls, type(ls))

# Индексация в списках
# ls = [1,2,3,4,5, 'string', [True, False, None]]
# print(ls, len(ls))
# print(ls[1], ls[2])
# print(ls[4:]) #[5, 'string', [True, False, None]]

# ls = [1,2,3,4,5, 'string', [True, False, None]]
# print(ls[6][:2]) #[6] - индекс списка, [:2] - обращение по индексу внутри списка

#Цикл for
# ls = list(range(1,11))
# print(ls)
# for num in ls:
#     print('hello world')
#     print(num)

# ls = ['JOhn', 'Sans
# for x in ls[1:]:
#     print(f'welcome back, {x}!')
#     print('100')
# print('2')

# ls -> 1, 21 -> для четных чисел вытащить квадрат числа а для нечетных чисел нуэно вытащить куб числа
# ls = list(range(1, 21))
# print(ls)
# for num in ls:
#     if num % 2 == 0:
#         print(f'Число четное, квадрат: {num**2}')
#     else:
#         print(f'Число нечетное , куб : {num**3}')

#-----------------------------------------------------------------------------------------------------------------------
# Методы списков:
# print(dir(list))
# append(element) - Добавляет элемент в конец списка
# ls = [1,2,3]
# print(ls)
# ls.append(4) #append принимает только 1 элемент за раз
# ls.append(5)
# ls.append('fwjrnm')
# ls.append([True, False])
# print(ls)

#extend(object) - Расширает список
# ls = [1,2,3]
# ls.append('Hello') # - просто добавляет в конец списка
# print(ls)
# ls.extend('hello', 'jejfen') #- дробит элемент по 1 и добавляет поочередно в конец списка
# print(ls)
# ls.extend([1,2,3])
# ls.extend(str(56453))
# print(ls)

# ls = [1,2,3]
# ls1 = [4,5,6]       Конкатенация тоже работает
# print(ls + ls1)

# #sort() - сортирует список если передать reverse=True, 
# то список отсортируется в убывающем порядке

# from random import randint
# ls = []
# for x in range(0, 100):
#     num = randint(0,100)
#     ls.append(num)
# print(f'Before: {ls}')
# ls.sort(reverse=True)
# print('After:')
# print(ls)

# ls = ['John', 'Deyneris', 'Tirion', 'Acnore']
# ls.sort(key=len, reverse=True) Сортировка по длине с помощью key
# print(ls)

# insert(index, element) - Добавляет элемент по указанному индексу, 
# работает как и apprnd, но добавляет по заданному индексу
# ls = ['string', 2, 3, 4, False]
# ls.insert(0,1) # если указать слишком большой индес то элемент добавится в конец
# print(ls)

# rermove(element) - Удаляет элемент из списка, если такого нет то выводится ошибка
# pop([index]) - Удаляет и возвращает элемент из списка по index, но если index не передать то удаляет последний элемент
# ls  = [5,2,3,4,4,5,6,5,5,]
# # print(ls)
# # ls.remove(5) - Удаляет только первый элемент 5
# # # print(ls)
# # print(5 in ls)
# # while 5 in ls:
# #     ls.remove(5) - удаляет все 5
# # print(ls)

# ls = [5,1,2,4,5,5]
# # print(ls.pop(5)) #5
# # print(ls.remove(5)) # None
# deleted = ls.pop()
# print(ls)
# print(deleted)

# update-----------------------------------------------------------------------

# ls  = [1, 'g', 3]
# print(ls)
# ls[0] = 2 # обратились по индексу и изменили на 2
# print(ls)
# ls.reverse()
# print(ls)
# print(ls[::-1])

# pizza = ['first_item', 'second_item', 'third_item', 'fourth_item', 'fifth_item', 'sixth_item']
# spisok = []
# for x in pizza:
#     if not x.startswith('f'):
#         spisok.append(x)

# print(spisok)



# string = input()

# if string is string.isdigit():
#     print('is digit')
# elif string is string.isalpha():
#     print('is alpha')



# suitcase = []
# suitcase.append('футболка')
# suitcase.append('шорты')
# suitcase.append('сланцы')
# suitcase.append('очки')
# suitcase.append('кепка')
# suitcase.pop()
# suitcase.insert([0],'kepka')




# list1 = [1,2,3,4,5,6,3,3443]
# # list2 = [3,4,5,66,7,88,7,8,6]
# # new_list = list1 + list2
# # print(new_list)
# new_ls = list(filter(str, list1, map(lambda x: x ** 2 if x % 2 == 0 else None,list1))) 
# print(new_l

# def fact(n):
#     res = 1
#     for i in range(1, n + 1):
#         res *= i
#     return res

# print(fact(6))
# print(fact(4))

print(dir(list))