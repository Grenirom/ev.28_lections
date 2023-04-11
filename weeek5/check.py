# # dict_ = {'a': 1, 'b': 2, 'c': 1}
# # del dict_['b'] 
# # print(dict_)
# dict_ = {'a': 32, 'b': 56, 'c': 37, 'd': 21}
# ls = list(dict_.values())
# print(max(ls))

# dict_ = {'a': 32, 'b': 56, 'c': 37, 'd': 21}
# ls = list(dict_.values())
# print(min(ls))
# dict1 = {'a': 3, 'b': 4, 'c': 9, 'd': 5, 'e': 6}
# dict2 = {}
# for k,v in dict1.items():
#     if v % 2 > 0:
# #         dict2.setdefault(k,1) #Изменение значений в словаре
# #     else:
# #         dict2.setdefault(k,v) # 
# # print(dict2)



# #-----------------ФУНКЦИЯ CLEAR-------------------------------------------------
# # dict_ = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# # dict_2 = {}
# # for k,v in dict_.items():
# #     if v == None:
# #         dict_2.setdefault(k,v)
# #         dict_.clear()
# #         dict_ = dict_2
# # print(dict_)

# #--------------------------------------------------------------------------------------------------
# # dict_ = {'Murat': 24, 'Erjan': 21, 'Karina': 24, 'Altynai': 17, 'Aibek': 16}

# # # for i in dict_:
# # #     if dict_[i] > 17:
# # #         print(f'{i} You can come in')
# # #     else:
# # #         print(f'{i} You cant come in!')
# # for i,v in dict_.items():
# #     print(i, 'i')
# #     print('v', v)
# #     if v > 17:
# #         print(f'{i} you can come in')
# #     else:
# #         print(f'you can\'t come in!')
# #-----------------------------------------------------------------------------------------
# # b ={}
# # a = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}
# # for key, value in a.items():
# #     for i_in, j_in in value.items():
# #         b[key] = j_in
# # print(b)
# #------------------------------------------------------------------------------------------
# # fruit = {'orange': 230, 'apple': 247, 'banana': 120}
# # # for i in fruit.copy():
# # #     if fruit[i] % 2 == 0:
# # #         fruit.pop(i)
# # # print(fruit)
# # for k,v in fruit.copy().items():  #copy() чтобы словарь не менял свой размер и не выходила ошибка
# #     if v % 2 == 0:
# #         fruit.pop(k)   #метод pop принимает только ключ
# # print(fruit)
# #-----------------------------------------------------------------------------
# # dict_ = {}
# # for i in range(1,10):
# #     dict_[i] = i **2
# # print(dict_)
# #-------------------------------------------------------------------------------------------
# # my_dict = {'first': {'a': 1}, 'second': {'b': 2}}
# # s = {}
# # for key,value in my_dict.items():
# #     for in_v in value.values():
# #         s[key] = in_v
# # print(s)
# #----------------------------------------------------------------
# # dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# # sorted_ = sorted(dict_.values())
# # sorted_dict = {}
# # for i in sorted_:
# #     for key,value in dict_.items():
# #         if value == i:
# #             sorted_dict[key] = value
# #             break
# # print(sorted_dict)
# #-----------------------------------------------------------------------------------------
# # num = int(input('Введите число'))
# # if num < 0:
# #     raise Exception('сумма не может быть отрицательной')
# #-------------------------------------------------------------------------------------------
# #                   task 24 lists
# # res = []
# # size = 3 
# # for i in range(1,size+1):
# #     grid = []
# #     for j in range(1, size+1):
# #         grid.append(j)
# #     res.append(grid)
# # print(res)
# #*---------------------------------------------------
# # for i in range(1,10):
# #     for j in range(1,11):
# #         print(f'{i}x{j} = {i*j}\n')

# #-------------------------------------------------------
# #       УГАДАЙ ЧИСЛО

# from random import randint
# name = input('Здравствуй! Введи свое имя:')
# choice = input(f'{name} ты хочешь играть?(yes/no):')
# rand = randint(1,10)
# i = 3
# tries = 0

# while i > 0:
#     if choice.lower().strip() == 'yes':
#         print('Приступим!')
#     else:
#         print('Хорошо, пока!')
#         break
    
#     print()
#     numg = int(input('Введи загаданное число(в диапозоне от 1 до 10):'))
#     print()
#     if numg == rand:
#         tries += 1
#         print(f'Ты угадал, с {tries} попытки!')
#         choice = input('ты хочешь продолжить игру?(yes/no):')
#         if choice.strip().lower() == 'yes':
#             tries = 0
#             rand = randint(1,10)
#             i = 3
#             print()
#         else:
#             print('Пока!')
#             break
#     else:
#         i -= 1
#         tries += 1
#         print(f'Ты не угадал, у тебя осталось {i} попытки!')
#         if i == 0 and tries == 3:
#             print(f'Загаданое число -- {rand}')
# #если что то упустил, прошу понять и простить


# dict_ = {'Bootcamp': 8, 'Makers': 6, 'coding': 6, 'hello': 5}
# max_ = max(dict_.values())
# print(max_)
# for k in dict_.keys():
#     if dict_[k] == max_:
#         print(k)
#------------------------------------------------------------
dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}}
dict2 = {}
for k,v in dict1.items():
    for in_v, in_k in v.items():
        del in_v
        
#         dict2.setdefault(k, in_v * in_v)
# print(dict2)

# list_ = ['hello', 23, 56, 'world', 928, 'Makers', 456, 'word', 223, 89, 'bootcamp', 'coding']
# dict_ = {}
# for i in list_:
#     dict_.setdefault(i)
#     for k,v in dict_.items():
#         print(k)
                      # task 16

# a = int(input()) 
# b = int(input()) 
# c = int(input()) 
# if a <= b and a <= c and b <= c: 
#     print(a,b,c) 
# elif a <= c and a <= b and c <= b: 
#     print(a,c,b) 
# elif b <= a and b <= c and a <= c: 
#     print(b,a,c) 
# elif b <= c and b <= a and c <= a: 
#     print(b,c,a) 
# elif c <= a and c <= b and a <= b: 
#     print(c,a,b) 
# elif c <= b and c <= a and b <= a: 
#     print(c,b,a) 
# else: 
#     print(a,b,c)

# a1, b1, c1 = int(input()), int(input()), int(input()) # множественное  присваивание
# c = max(a1, b1, c1) # выводим максимальное значение 3х чисел
# b = min(a1, b1, c1) #выводим минимальное значение из 3х чисел
# a = sum([a1, b1, c1]) - min(a1, b1, c1) - max(a1, b1, c1) # какая то формула по всей видимости
# if c >= a + b: #
#     print('impossible') 
# elif c**2 == a**2 + b**2: #
#     print('rectangular') 
# elif c**2 < a**2 + b**2: #
#     print('acute') 
# elif c**2 > a**2 + b**2: #
#     print('obtuse')


try:
    age = int(input())
    if age < 18:
        
        raise ValueError('Доступ запрещен')
except:
    print('Введён некорректный возраст')
else:
    print('Спасибо')
finally:
    print('До свидания!')