#встроенные функции
# анонимная функциия  - lambda (обычная функция с одной особенностью, у нее нет имени)
# принимает сколько угодно параметров но всегда возвращает одно выражение
# def hello():
#     return 'hello'

# # print(hello())

# x = lambda: 'hello'
# print(x())

# x = lambda a, b, c: (a * b) % c
# print(x(5,5,5))
#----------------------------------

# x = lambda num1, num2, degree=None: (num1 * num2) ** degree if degree else num1 * num2
# print(x(2,2,3))

# def myFunc(n):
#     return lambda num: num * n

# my_doubler = myFunc(2)
# print(my_doubler(50))


# dict_ = {
#     'john': 500,
#     'tirion': 160_000,
#     'tom': 150,
#     'danchar': 20,
#     'ayana': 100_000,
# }
# print(dict_.items())
# new_dict = dict(sorted(dict_.items(), key=lambda x: x[1], reverse=True))
# print(new_dict)
#---------------------------------------------


#map(function, iterable) - применяется к каждому элементу внутри iterable функцию,
# которуую мы ей передаем в function, закидывая в результат те данные, которые возвращает функция.
# В результате мы получаем mapobject(iterator), в котором хранятся все наши данные.

# ls = ['1', '2', '3', '4']  #'one', 'two', 'three', 'four'

# new_ls = list(map(int, ls))             #list(map(lambda x: x.capitalize(), ls))
# print(new_ls)
#---------------------------------------------
# names = ['john', 'aria', 'baku', 'bakberdi', 'lilo']

# #hwllo, mr/mrs John
# new = list(map(lambda x: f'hello mr/mrs {x}', names))
# print(new)
#-----------------------------------------------


'''
Функция высшего порядка - функция, которая принимает в качестве
 аргумента другую функцию
'''

'''
filter(function, iterable) - применяет ко всем элементам iterable функцию, которую мы
передали и возвращает filterobject(итератор) только с теми элементами, для которых функция вернула
True
'''

# ls = ['one', 'lili', 'oleg', 'billie', 'tirion']
# res = list(filter(lambda x: len(x) > 4, ls))
# print(res)
#--------------------------------------------------
'''
enumerate(iterable) - пронумеровывает каждый элемент внутри 
iterable ее собственным индексом
'''

# ls =['str1', 'str2', 'str3']
# new_list = list(enumerate(ls))
# print(new_list)


# ls = [1,2,3,4,5]
# ls1 = list(filter(lambda x: x ** 2, ls))
# print(ls1)

# ls = [1,2,3,4,5]
# ls1 = list(map(lambda x: x ** 2, ls))
# print(ls1)