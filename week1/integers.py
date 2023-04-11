#pow - возведение в степень
#pow (num1, num2, <mod>)
#print(pow(5, 10, 65))
#print(5 ** 10 % 65)


#a = 5
#b = 2
#res = pow(a, b, 12)
    # 5 ** 2 = 25 % 12 = 1
#print(res)

#round() - окуругление числа с плавающей точкой 
#a = 5.7899333
#print(round(a, 2))  # 4 это количество чисел за точкой которые нужно тоже округлить

#abs() - абсолютное значение числа -> abs(-5) -> 5
                                        #|-5| -- 5

#a = abs(-16)
#b = abs(15)
#print(a, b)

#divmod(a, b) -- онавыводит 2 числа, первое число это результат целочисленного деления (//) а на b, 
#а второе это модульное деление(%)

#rea = divmod(5, 2)
#print(rea)
#print(5 // 2, 5 % 2)

#получение квадратного корня
# import math

# a = 5
# print(round(math.sqrt(a), 2))
# res = math.sqrt(a)
# print(round(res, 2))


# множественное присваивание 
#оператор присваивания (=)
# a = 5
# b = 15
# c = None
# print(a, b)

# # c = a
# # a = b
# # b = c
# a, b = b, a
#         #15, #5


# print('a:', a,'b:', b)

#множественное присваивание 
# num1, num2, num3 = input('Num1:'), input('Num2:'), input('Num3:')
# print(num1)
# print(num2)
# print(num3)

# from math import pi 


# import math

# # print(pi, type(pi))
# r = int(input('Введите радиус:'))
# resP = 2 * r * pi
# resS = pi * (r ** 2)
# print('Площадь окружности:', resS)
# print('Периметр окружности:', resP)


# from random import randint
# print(randint(1, 10))
#1,2,3,4,5,6,7,8,9,10

# name = input('Введите свое имя:')
# last_name = input('Введите свою фамилию:')
# num = randint(1_000_000, 9_999_999)
# # print(name, last_name, num)
# print('123'+ 'ev.28')

# res = name + last_name + str(num)
# print(res)


# from random import randint

# num = randint(1, 10)
# print(num)
# i = 0
# while i < 3:
#     number = int(input('Guess the number:'))
#     if number == num:
#         print('Ты угадал!')
#         break
    
#     # i = i + 1
#     i += 1 #increment

# first = 1
# second = 2 
# third = 3
# first, second, third = second, third, first
# print(first, second, third)

# lenght = 5 
# height = 6
# p = 2 *( lenght ** 2 + height ** 2) ** 0.5 + 2 ** lenght
# s = lenght * height / 2
# print(p, s)

# positive = 12
# negative = -12
# print(abs(positive, negative))
# print(abs(negative))

# a,v,e = 53,13,355
# print(a,v,e)



