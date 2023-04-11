# Декораторы - функция которая позволяет без изменения кода функции расширить ее функционал

# def decorator(func):
#     print(func)
#     func()

# def hello():
#     print('hello stranger!')

# def john():
#     print('my name is john snow! I\'m king of North!')

# decorator(hello)
# print('!!!!!!!!!')
# decorator(john)
#----------------------------------------------------------------------------------------
# pytonic way -> @
# синтаксический сахар - красота кода



# def decorator(func):
#     def wrapper():
#         print(f'Мы вызвали функцию: {func.__name__}')
#         func()
#     return wrapper

# @decorator                                  #@decorator -> decorator(hello)
# def hello():
#     print('hello stranger!')

# @decorator
# def john():
#     print('my name is john snow! I\'m king of North!')
# hello()
# print('!!!!!!')
# john()
#-------------------------------------------------------------------------------------
# def benchmark(func):
#     def wrapper(*args, **kwargs):
#         import time
#         start = time.time()
#         func(*args, **kwargs)
#         finish = time.time() 
#         print(f'Время выполнения функции: {func.__name__}, заняло {finish - start}')
#     return wrapper

# @benchmark
# def loop():
#     i = 0
#     range_number = 1_000_000
#     while i < range_number:
#         i += 1
# @benchmark
# def add():
#     i = 0
#     range_number = 100_000_000
#     ls = []
#     while i < range_number:
#         ls.append(i)
#         i += 1
#     # print(ls)



# loop()
# add()
#------------------------------------------------------------------------
# def bold(func):
#     def wrapper(*args, **kwargs):
#         res = '<bold>' + func(*args, **kwargs) + '</bold>'
#         return res
#     return wrapper

# def div(func):
#     def wrapper(*args, **kwargs):
#         res = '<div>' + func(*args, **kwargs) + '</div>'
#         return res
#     return wrapper

# @bold
# @div
# def str_(name):
#     return name



# print(str_('John Snow'))
#------------------------------------------------------------------------------
# def trace(func):
#     def wrapper(*args, **kwargs):
#         print(f'Trace: вызвала {func.__name__}() \nона приняла {args}, kwargs:{kwargs}')
#         original_result = func(*args, **kwargs)
#         print()
#         print(f'Trace: вызвала {func.__name__}() \nона вернула {original_result}')
#         print()
#         return original_result
#     return wrapper

# @trace
# def say(name, address):
#     return f'{name} --> {address}'

# @trace
# def hello(name, last_name, country):
#     return f'Hello {name} {last_name} from {country}!'



# say('Sherlock Holms', 'BakerStreet 221b')
# hello('Gomer', 'Simpson', 'Canada')
#-----------------------------------------------------------------------------------------------
list1 = [1,2,3,4,5,6,3,3443]
list2 = [3,4,5,66,7,88,7,8,6]
new_list = list1.join(list2)
print(new_list)