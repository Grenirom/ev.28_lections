# while <expression>:
#     <body> 
# i = 0
# while i < 10:
#     i += 1
#     print(f'Цикл повторился {i} раз!')

# ls = list(range(1,51))
# print(ls.reverse())
# while ls:
#     print(ls.pop())
# name1 = ''
# name2 = ''
# i = 0
# while name1.lower() != 'john' and name2.lower() != 'raychel':
#     name1 = input('Введите имя1:')
#     name2 = input('Введите имя2:')
#     print()
    
    
#     if i >= 5:
#         print('Цикл остановлен!')
#         break # Принудительная остановка цикла 
#     i += 1
# else: # Оператор который сработает только если в While прилетит False
#     print('ты угадал!')
#----------------------------------------------------------------
# user = {'username': 'JohnSnow', 'password': 'ilovepython'}
# i = 3
# # password = None
# while password := input(f'{user["username"]} vvedite parol\':') != user['password']: #маржовый оператор, 
#     # позволяет объявлять переменную в цикле
#     # password = input(f'{user["username"]} vvedite parol\':')
#     i -= 1 
#     if i == 0:
#         print('Вы заблокированы!')
#         break
# else:
#     print(f'{user["username"]} вы успешно зашли в систему!')
#---------------------------------------------------------------------------------
#for<variable> in <iterable object>:
    # <bofy>
# list_ = [0,1,2,3,4,5,6,7,8,9]
# i = iter(list_)
# print(i)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i)) #5
# print(next(i)) #6
# print(next(i)) #7
# print(next(i)) #8
# print(next(i)) #9
# print(next(i)) # Stopiteration
#------------------------------------------------------------------------------------------
# import random
# ls = []
# for x in range(1,101):
#     ls.append(random.randint(1,50))
    
# print(len(ls))
# ls  = set(ls)
# ls = list(ls)
# print(ls)
# print(len(ls))
#------------------------------------------------------------------------------------------
# a = (1,) # литералами tuple являются скобки и запятые
# print(a)
# a,b,c = 1,2,3
# print(a, b, c)
#--------------------------------------------------------------------------
# ls = ['Tirion', 'Bilal', "John", 'Sansa', 'Sonya', 'jack']
# for x in ls:
#     if x == 'Bilal':
#         continue  # позволяет пропустить прохождение по указанному элементу
#     print(f'Hello ms/mrs {x}!')
#--------------------------------------------------------------------------
# i = 0
# while i < 100:
#     i += 1
#     if i % 2 >= 1:
#         continue
#     print(i)
#----------------------------------------------------------------


# num = 1_000_000_000
# res = []

# for x in range(1, int(num ** 0.5) + 1):
#     if num % x == 0:
#         res.extend({x, num // x})
# res.sort()
# print(res)

