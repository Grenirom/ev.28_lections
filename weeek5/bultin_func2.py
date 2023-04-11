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
