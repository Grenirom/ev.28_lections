# list comprehensions - Это генераторы списков,
# упрощенный подход к созданию списков который задействует в себе цикл for, 
# а так-же констрункцию if для определения того что в итоге попадет в наш список

# list -> 0 - 200, -> num % 2 == 0
# ls = []
# for x in range(0,201):
#     if x % 2 == 0:
#         ls.append(x)

# ls = [x for x in range(0,201) if x % 2 != 0]    # List comprehension
# print(ls)
#--------------------------------------------------------------------------------------
# list: 0 - 300 -> num % 2 == 0, num % 3 == 0
# ls = [2 for x in range(0,301)] #if x % 2 == 0 and x % 3 == 0]
# print(ls)

# ls = []
# for i in range(0,301):
#     if i % 2 == 0 and i % 3 == 0:
#         ls.append(i)
# print(ls)
#-------------------------------------------------------------------------------------------
# list: 0 - 100, num % 2 == 0 ->x **2. i % 3 == 0, x = x**3
# ls = []
# for x in range(1,101):
#     if x % 2 == 0:
#         ls.append(x ** 2)
#     elif x % 3 == 0:
#         ls.append(x ** 3)
# print(ls)

# ls = [x ** 2 if x % 2 == 0 else x ** 3
#       for x in range(0,101)
#       if x % 2 == 0 and x % 3 == 0]
# print(ls)





#---------------------------------------------------------------
# new_list = [wxpression for item in iterable <if condition == True>]
# ls = [str(), print(), input()]
# ls = [str(i * 2) for i in range(0,11)]
# print(ls)
#--------------------------------------------------------------------------------
# ls = [[1,2,3], [4,5,6], [7,8,9]]
# #result = [1,2,3,4,5,6,7,8,9]
# res = []
# for x in ls:
#     for item in x:
#         res.append(item)
# print(res)         #[1, 2, 3, 4, 5, 6, 7, 8, 9]
#      COMPREHENSION
# ls = [[1,2,3], [4,5,6], [7,8,9]]
# res = [item for x in ls for item in x]
# print(res)      #[1, 2, 3, 4, 5, 6, 7, 8, 9]
#----------------------------------------------------------------------------------

# from datetime import datetime
# start = datetime.now() # 19:55
# # ls = [x for x in range(0,100_000_000)]
# # # code ..... (3 sec)
# # # ls = []
# # # for x in range(0,100_000_000):
# # #     ls.append(x)

# # finish = datetime.now() #19:57
# # print(finish - start)
# #--------------------------------------------------------------------------------------
# #set comprehensions
# # set1 = {x for x in range(1,101)}
# # print(set1, type(set1))
# #------------------------------------------------------------------------------------
# #dict comprehensions
# # dict1 = {
# #     key: value,
# #     key: value,
# # }
# # dict1 = {x: x**2 for x in range(0,16)}
# # print(dict1)
# # names = ['john', 'tirion', 'sansa', 'david']
# # dict1 = {x: len(x) for x in names}
# # print(dict1)
# #------------------------------------------------------------------------------------------
# # res = {}
# # dict1 = {
# #     'Soke': {'history': 99, 'physics': 95,'math': 93},
# #     'Omoke': {'history': 84, 'physics': 88, 'math': 83},
# #     'John': {'history': 100, 'math': 99, 'physics': 87}

# # }
# # # for key,value in dict1.items():
# #     for inner_key,inner_value in value.items():
# #         if max(value.values()) == inner_value:
# #             res[key] = inner_key
# # # print(dict1)
# # print(res)

# dict1 = {
#     'Soke': {'history': 99, 'physics': 95,'math': 93},
#     'Omoke': {'history': 84, 'physics': 88, 'math': 83},
#     'John': {'history': 100, 'math': 99, 'physics': 87}

# }
# res = {key: inner_key for key,value in dict1.items() for inner_key,inner_value in value.items() if inner_value == max(value.values())}
# print(res)

        

        

#-----------------------------
# #           TASK
# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ]
# # new_list = ['shorter' if len(list_name) <= 4 else 'longer' for i in list_name]
# for i in list_name:
#     print(len(i))
#----------------------------
# n = int(input('Введите число от 1 до 10:'))
# dict_ = {x for x in range(1,501) if x % 2 == 0}
# print()

sqr = {num: num * num for num in range(10)}
print(sqrсщ)