# dict() - словарь -> упордоченная коллекция элементов(python3.7 -> ordered).
#  Каждый элемент внутри словаря ввиде пары{ключ: значение}

# ассоциативный массив, hash table, object(js), structure
# == dictionary(py)
#ключами могут быть только неизменяемые типы данных
# и в словаре сохраняются только уникальные ключи.
#тогда как значениями могут выступать любые типы данных и значения могут повторяться

this_dict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1967
}

# print(this_dict)
# print(type(this_dict))
# print(this_dict['model'], this_dict['year'])
print(this_dict['brand'])

# this_dict['motor'] = 'GTE Turbo' #Добавление нового ключа и значения к нему
# print(this_dict['motor'])
# this_dict['brand'] = 'Tesla' # если укажем существующий ключ
# #то через равно можно перезаписать значение
# print(this_dict)
# a = {} #dict()
# a = {1,2,3,4} #set()
# print(type(a))

# a = {}
# b = dict()
#--------------------------------------------------------------------------------------------
#Методы словарей
# print(dir(dict))

# items, keys, values
# user_info = {
#     'first name': 'john',
#     'last_name': 'Snow',
#     'age': 24,
#     'email': 'johnsnow@gmail.com',
#     'role': 'admin',
# }


# print(user_info.keys())  #Список наших ключей, у словаря нет индексации
# ls = user_info.keys()
# ls = list(ls)   # Для того чтобы получить ключи по индексам, создаем переменную из списка
# print(ls[2:])
#--------------------------------------------------------------------------------------
# ls = list(user_info.values())        #Вытаскивает значения 
# print(ls)
#--------------------------------------------------------------------------------------
# items = user_info.items()   # Вытаскивает и ключ и значение 
# print(items)
#--------------------------------------------------------------------------------------
# for key, value in user_info.items():
#     print(f'keys: {key}, values: {value}')

# for items in user_info.items():
#     print(f'keys: {items[0]}, values: {items[1]}')       # Образение по индексам
#--------------------------------------------------------------------------------------
# for key in user_info.keys():
#     print(key)
# #--------------------------------------------------------------------------------------
# for value in user_info.values():
    # print(value)
#----------------------------------------------------------------------------------------
# dict_ = {'name': 'jack', 'age': 17}
# print(dict_)
# dict_['name'] = 'John' # изменение значений в словаре
# dict_['age'] = 24 # то же самое 
# dict_['address'] = 'WinterFell' # и это 
# print(dict_)
# dict_.update({'age': 25, 'address': 'BlackCastle'}) # можно изменить значения в ключах с помощью метода .update
# print(dict_)                                        # тут мы все это делаем в одну строчку
#---------------------------------------------------------------------------------------------
#Получение данных со словаря 
dict_ = {1: 'Pizza', 2: 'Burgers', 3: 'Steaks'}
   #обращение по ключу
print(dict_.get(3)) #Получение с помощью метода, если указать несуществующий ключ, выдаст None
#-----------------------------------------------------------------------------
# setdefault - работает как get, но если нет такого ключа
# то он создает новую пару из этого ключа
# dict_ = {1: 'Pizza', 2: 'Burgers', 3: 'Steaks'}
# print(dict_.setdefault(4, '   Manty')) #Создание нового ключа и присвоение ему нового значения 
# print(dict_)                            
#--------------------------------------------------------------------------------------------
# создание словаря - fromkeys
# ls = list(range(1, 100))
# new_dict = dict.fromkeys(ls, 'Value')
# print(new_dict)
#--------------------------------------------------------------------------------------------
#Удаление элементов - popitem, pop
# pop(<key>) - удаляет пару по ключу который мы передали
# dict_ = {'name': 'John', 'last_name': 'Snow'}
# print(dict_)
# removed = dict_.pop('last_name') # вызываем метод и в скобках указываем ключ, и удаляем и значение и ключ
# print(dict_)
# print(removed)
#--------------------------------------------------------------------------------------------
# popitem - Удаляет последнюю пару
# dict_ = {'name': 'John', 'last_name': 'Snow'}
# dict1 = {'last_name': 'Snow', 'name': 'John'}
# print(dict_)
# print(dict1)
# removed = dict_.popitem()
# print(dict_)
# print(removed)
#-------------------------------------------------------------------------------------------------






# roles = {
#     0: 'Admin',
#     1: 'Customer',
#     2: 'Vendor', 
# }

# users = {
#     1: {
#     'id': 1, "role": roles[2], "username": 'Tirion',
#     },
#     2: {
#     'id': 2, 'role': roles[0], 'username': 'John'
#     },
#     3:{
#     'id': 3, 'role': roles[1], 'username': 'Raychel'
#     }
# }

# product = {
#     'id': 1,
#     'title': 'Samsung Galaxy A51',
#     'description': 'Lorem Ipsum',
#     'price': 250 ,
# }
# print(product)
# id_user = int(input('Введите Id: ')) #1
# if users[id_user]['role'] == roles[0]:
#     product['description'] = input('Введите новое описание: ')
# else:
#     print('У вас нет нужных прав на это действие!')

# # print(product)
#--------------------------------------------------------------------------------------------

        # print(dir(int))
    # ind = str(i)
    # print(i)
    # print(ind)
    # print(dir(int))
#-------------------------------------------------------------------------------------------
# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6} 
# b = {}
# for k, v in a.items(): 
#     if v%2==0: 
#         b.setdefault(k, 2) 
#     else: 
#         b.setdefault(k,v) 
# print(b)
#-----------------------------------------------------------------------------------
# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# a = {1: None, 2: 'b', 3: None} 
# a.items()
# for k,v in list(a.items()):
#     if type(v) != int and type(v) != str:
#         del a[k]
# print(a)
#-----------------------------------------------------------------------------------
# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
# c = {}
# a.items()
# for k,v in list(a.items()):
#     b = v/5
#     c.setdefault(k, b)
# print(c)
#-----------------------------------------------------------------------------------
# a = {'apple': 2, 'orange': 5, 'banana': 10} 
# ls = a.items()
# ls = list(ls)
# for k,v in ls:
#     if v % 2 == 0:
#         del a[k]
    
# print(a)
#------------------------------------------------------------------------------------
# a = {'a': 1, 'b': 2, 'c': 3}
# a.items()
# for k,v in ls:
# #     if v == str:
# a = {'a': 1, 'b': 2}
# for v in a.values():
#     int(v + v)
# print(v)



# dict1 = {25: 'apple', 26: 'orange', 27: 'banana'}
# dict2 = {}
# for k,v in dict1.items():
#    dict2.setdefault(k ** 2, v)
# print(dict2)

# list_ = ['Bootcamp', 'Makers', 'coding', 'hello']
# dict_ = {}
# for i in list_:
#     ls = len(i)
#     # print(ls)
#     dict_.setdefault(i, ls)

# print(dict_)
    
# dict_ = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}} 
# # dict_ = {k:(v[v1]) for k,v in dict_.items()} 
# # print(dict_) 
# for k,v in list(dict_.items()): 
#     for v2 in v.values(): 
#         dict_[k] = v2 
#         print(dict_)

dict1 = {'1': 12, '1': 2, '2': 123}
print(dict1)
