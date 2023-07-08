# # Задагие №3 -----------> 1 point
# num = int(input())
#
# num_str = str(num)
# temp = [int(i) for i in num_str]
# flag = 'No'
#
# if temp[0] > temp[1]:
#     if temp[1] > temp[2]:
#         if temp[2] > temp[3]:
#             flag = 'Yes'
# print(flag)

#1
# #2 --------->1 point
# def kvad():
    # x = input('Enter num: ')
    # print('perimetr',int(x)*4)
    # print('ploshad',int(x)**2)
    # print('diagonal',int(x)*(2**0.5))

# kvad()


#ЗАдание 1 --------> 1 point
# a = 0
# b = 2
# c = 5
# a,b,c = a + b, c - b, a + b + c
# print(a)
# print(b)
# print(c)

# Задание №4-----------> 0 points
# for i in range(10000, 100000):
#     temp = str(i)
#     num_str = [int(i) for i in temp]
#
#     sum_digits = sum(num_str)
#     if i % 2 == 0:
#         if num_str[2] % 2 != 0:
#             if sum_digits % 4 == 0:
#                 print(i)

# 8.---------> 0.5
#
# for i in range(1, 51):
#     if i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     if i % 3==0 and i % 5 == 0:
#         print('FizzBuzz')

#6================>0.5
# geo_logs = [{'visit2': ['Deli', 'India']}, {'visit3': ['Vlad', 'Russia']}, {'visit9': ['Kursk', 'Russia']}]
# for i in geo_logs:
#     for x,y in i.items():
#         for d in y:
#             if d == 'Russia':
#                 print(x)

# 7.-----------> 0,5 point

# x = int(input())
# a = int(input())
# k = int(input())
#
# print(f'{a / x} кг за {a} руб, {k / a} можно купить кг за {k} руб')
#
#
# 5 ---------> 0.5
a = '1234'
b = a[-1] + '23' + a[0]
print(b)