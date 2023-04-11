# def decorator(func):
#     def wrapper():
#         print(f'THis function named: {func.__name__}')
#         return func()
#     return wrapper

# @decorator
# def hello():
#     print('Hello')

# hello()
# def sq(func):
#     def wrapper(num):
#         nums = func(num)
#         return list(map(lambda x: x ** 2, nums))
#     return wrapper

# @sq
# def func(num: int):
#     return list(range(1, num))

# @sq
# def func2(num):
#     return list(range(1, num, 2))


# # print(func(4))
# print(func2(6))

#---------------------------------------------------------------------------


