# zip(iterables) - она соединяет каждый элемент 
# итерируемых объектов между собой в тип данных tuple и возвращает итератор


# ls1 = [1, 2, 3, 4]
# ls2 = [100, 200, 3003, 2345]

# res = dict(zip(ls1, ls2))
# print(res)

# ls1 =  [1,2,3,4,5]
# ls2 = [1,2,3,4,5,6]
# ls3 = [10,203,40,60,234]

# res= list(zip(ls1, ls2, ls3))

# print(res)
#-------------------------------------------------------------
"""
zip - для создания словарей 
"""

# d_keys = ['hostname', 'location', 'vendor', 'model', 'IP']
# data = {
#     'oktbr': ['bishkek_oktbr', 'Gorkogo 212', 'Vefa', 'Cisco', '10.43.21.34'],
#     '1may': ['bishkek_1may', 'jibek-jolu 212', 'white house', 'Cisco', '1221.321.324.1'],
#     'svdrl': ['bishkek_svrdl', 'ahunbaeva 212', 'TC', 'Cisco', '33.43.114.34']
# }
# bishkek_data = {}
# for k in data:
#     bishkek_data[k] = dict(zip(d_keys, data[k]))

# print(bishkek_data)
#----------------------------------------------------------------------------------------
"""
all(), any()

all(iterable) - возвращает True, если все элементы итерируемого объекта внутри истина,
иначе возвращает False
"""

# ls = [6,6,0]
# print(all(ls))  # False

# ip = '10.255.0.155' # True
# ip1 = '10.124.0y.202' # False
# result = all(x.isdigit() for x in ip1.split('.'))
# print(result)

"""
any - возвращает True, если хотя бы один элемент истина
"""

# ls = [1,2, [1,2,3], 0]
# print(any(ls))
#------------------------------------------------
# ignore = ['rm -rf', 'sudo', 'reset', 'poweroff']
# command = input('Введите команду:')

# if any(x in command for x in ignore):
#     raise Exception('Blocked')
# print('It\'s ok!')
#-------------------------------------


# from random import choices
# from string import ascii_letters, digits
# from itertools import repeat

# symbols = '_()+-@#%'

# q_pass = int(input('Введите кол-во паролей:'))
# res = {
#     f(choices(ascii_letters, k=15), choices(digits, k=6), choices(symbols, k=2))
#     for f in repeat(lambda x, y, z: ''.join(set(x + y + z)), q_pass)
# }
# print(res)
# print(f'Quantity of passwords: {len(res)}')

# from statistics import mean

# print(f'Average len of passwords: {mean(len(x) for x in res)}')
#----------------------------------------------------------------------------
#                                  TASK 11
# a = range(1,50)
# result = list(map(lambda x: 'Fizz' if x % 3 == 0 else 'Buzz', a))
# print(result)
#----------------------------------------------------------------------------
#                                  TASK 12
# import functools
# list_ = [1,2,3,4,5,6,7]
# res = functools.reduce(lambda x, y: x if x > y else y, list_)
# print(res)
#-----------------------------------------------------------------------
#                                  TASK 13
# import functools
# list_ = [1,2,3,4,5,6,7]
# res = functools.reduce(lambda x, y: x if x < y else y, list_)
# print(res)
#----------------------------------------------------------------
#                                  TASK 14
# string = 'hello'
# res = tuple(enumerate(string))
# print(res)
#-----------------------------------------------------------------
#                                  TASK 15
# list_ = [-7, -2, 12, 32, 432, 23, 37, 11, 76, 0, -23, 45, -32, -56]
# res = list(map(lambda x: abs(x), list_))
# print(res)
#-----------------------------------------------------------
#                                  TASK 16
# list_ = ['hello', 123]
# res = list(map(lambda x: type(x), list_))
# print(res)
#------------------------------------------------------
#                                  TASK 17
# names = ['rauchel','john','peter','jessica','steven123','dandy34','kamest','potter']
# res = list(map(lambda x:x + ' ' + 'Python' if len(x) > 5 else x+ ' ' + 'JavaScript', names))
# print(res)
#--------------------------------------------------------
#                                   TASK 18
# list_ = ['123hello@gmail.com', '123', 'hello']
# check = '@gmail.com'
# res = list(map(lambda x: x if check in x else 'Not valid email', list_))
# print(res)
#-----------------------------------------------------
#                                  TASK 19
# string = 'hello'
# res = tuple(enumerate(string,1))
# print(res)
#---------------------------------------------------
#                                  TASK 20
# list1 = ['M', 'A', 'K', 'E', 'R', 'S'] 
# list2 = [236, 54, 33, 21, 89, 1]
# res = list(zip(list1, list2))
# print(res)
#-------------------------------------------------------------------
#                               TASK 21
# list_ = [-7, -2, 12, 32, 432, 23, 37, 11, 76, 0, -23, 45, -32, -56]
# res2 = []
# res1 = list(filter(lambda x: x if x > 0 else res2.append(x), list_))
# res3 = list(zip(res1, res2))
# print(res3)
#-----------------------------------------------------------
#                               TASK 22
# list_ = [0.334, 23.3443, 43.4, -13.44, 22.03, -11.033, 267.993, -3.24] 
# res=list(map(lambda x:round(x**2,3),list_)) 
# print(res)
#--------------------------------------------------
#                               TASK 23
# import functools
# list_ = ['a', 'n', 'n', 'a']
# res = functools.reduce(lambda x, y: x + y, list_)
# if res == res[::-1]:
#     print('YES')
# else:
#     print('NO')
