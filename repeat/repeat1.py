# num1 = 1

# while num1 >=0:
#     num1 = input('Введите число:') #int('54')
#     if num1[0] == '-' and num1[1:].isdigit():
#         num1 = int(num1)
#     else:
#         num1 = 1
#---------------------------------------------------------------------------------------------

# print('Встретилось отрицательное число!')

# from random import randint
# ls = []
# for x in range(0,100):
#     ls.append(randint(0,100))

# res = []
# for x in ls: # [5,6,7]
#     if x not in res:
#         res.append(x)
#         res.sort()
# print(res, len(res))
#-------------------------------------------------------------------------------------------

# Шахматная ладья ходит по горизонтали или вертикали. 
# Даны две различные клетки шахматной доски,
#  определите, может ли ладья попасть с первой клетки на вторую одним ходом.
# Программа получает на вход четыре числа от 1 до 8 каждое, 
# задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
# Программа должна вывести YES, если из первой клетки ходом ладьи 
# можно попасть во вторую или NO в противном случае.
# Вводить в порядке x1, y1, x2, y2

# x1 = int(input('введите первую координату ладьи:')) # по горизонтали
# y1 = int(input('введиет вторую координату ладьи:')) # по вертикали
# ladya = [x1,y1]

# x2 = int(input('введите первую координату куда идет ладья:'))
# y2 = int(input('введиет вторую координату куда идет ладья:'))
# target = [x2, y2]
# if x1 == x2 or y1 == y2:
#     print(True)
# else:
#     print(False)

# Задание 25
# Шахматный слон ходит по диагонали. Даны две различные клетки шахматной доски, определите, может ли слон попасть с первой клетки на вторую одним ходом. Программа должна вывести YES, либо NO
# Вводить в порядке x1, y1, x2, y2
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if x2 - x1 == y2 - y1:
#     print('YES')
# else:
#     print('NO')
#---------------------------------------------------------------------------------------------
import random
ls = ['Plov', 'Beshbarmak', 'Kuurdak', 'Lagman', 'Oromo']
p = 0
b = 0
k = 0
l = 0
o = 0
for x in range(0, 1_000_000):
    meal = random.choice(ls)
    # print(meal)
    if meal.lower() == 'plov':
        p += 1
    elif meal.lower() == 'beshbarmak':
        b += 1
    elif meal.lower() == 'kuurdak':
        k += 1
    elif meal.lower() == 'lagman':
        l += 1
    else:
        o += 1

print('Результаты голодных игр:')
# print(f'Plov: {p}\nBeshbarmak: {b}\nKuurdak: {k}\nLagman: {l}\nOromo: {o}')
dict_ = {'Plov': p, 'Beshbarmak': b, 'Kuurdak': k, 'Lagman': l, 'Oromo': o}
# print(dict_)
res = sorted(dict_.items(), key=lambda x: x[1], reverse=True)
print(res)
print(f'Победило блюдо: {res[0]} и оно набрало: {res[1]} очков!')
#--------------------------------------------------------------------------------------------
# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# 1) nums = [2,7,64,323]
# target = 9
# 0.1
# 2) nums = [4,11,2,5,1,6]
# tagret = 8

# nums = [4,11,2,5,1,6]
# target = 8
# for i in range(0, len(nums)):
#     # print(i)
#     # print(nums[i])
#     num = target - nums[i]
#     if num in nums:
#         if num != nums[i]:
#             print(f'ответ: {i}, {nums.index(num)}') #nums.index - способ нахождение индекса
#             break