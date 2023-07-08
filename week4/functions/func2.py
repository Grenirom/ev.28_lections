# # 'hello world! my name is john, last name is snow. nice to meet you!'
# str1 = 'hello world! my name is john, last name is snow. nice to meet you!'
# def get_reversed_text(text):
#     # print(text[::-1])
#     ls = text.split()[::-1]
#     # print(ls[::-1])
#     return ' '.join(ls)
    
# get_reversed_text(str1)
#---------------------------------------------------------------------------------------------------

# def sum_of_args(a,b,c=5,d=5): #параметры
#     return a + b + c + d

# result = sum_of_args(1,2,3,4)
# print(result)
# res = sum_of_args
# print(res(5,6))
#-------------------------------------------------------------------------------------------------
# ПОЗИЦИОННЫЕ И ИМЕНОВАННЫЕ АРГУМЕНТЫ
# def printParams(a,b,c):
#     print(a, 'is stored in param a')
#     print(b, 'is stored in param b')
#     print(c, 'is stored in param c')
    

# printParams(5,10,15)
# print()
# printParams(c=5, b=15, a=10)
# print()
# printParams(a=20, b=35, c=55)
#---------------------------------------------------------------------------------------------------

# def sum_of_args(a,b,c,d): #параметры
#     return a + b + c + d

# print(sum_of_args(5,10,23,53))  #arguments(позиционные аргументы)
# print(sum_of_args(4,23,c=11,d=66)) #keyword arguments(именованные аругемнты)
#---------------------------------------------------------------------------------------------------

# оператор '*'
# a = [1,2,3]
# b = [4,5,6]
# c1 = a + b   # делает то же самое
# c = [*a,*b]  # распаковываем 2 списка и соединяем в один
# print(c)
# print(c1)
#----------------------------------------------------------------------------------------
 # *args, **kwargs в функциях

# def printScores(student, *scores):
#     print(f'Name of student: {student}')
#     # print([*args])
#     print(f'AVG: {sum(scores) / len(scores)}')
#     for x in scores:
#         print('score:',x)

# printScores('john snow', 100,90,80,95,88) 
#-----------------------------------------------------------------------------------------
# def printPetNames(owner, **kwargs):
#     print(f'Owner name: {owner}')
#     # print(kwargs)
#     for pet, name in kwargs.items():
#         if type(name) == list:
#             print(f'{pet}:', *name)
#         else:
#             print(f'{pet}: {name}')

# printPetNames('John Snow', dog='Rex', cat='Garfild', fish=['Nemo', 'Dori', 'Batya', 'Leonardo'])
#--------------------------------------------------------------------------------------------------

# def get_some_data(a,b, *args, **kwargs):
#     print('Параметры a и b:', a,b)
#     print('аргументы:', [*args])
#     print('именованные аргументы:', kwargs)

# get_some_data(1,2,3,4,5, lang='Python', car='bmw')
#--------------------------------------------------------------------------------------------------

# def generate_random_string(len_):
#     import string as s
#     import random
#     # print(s.ascii_letters, s.digits)
#     symbols = s.ascii_letters + s.digits
#     resilt = list(
#         random.choice(s.ascii_letters + s.digits) for i in range(0, len_)
#     ) + list(random.choice(s.punctuation))
#     random.shuffle(resilt)
#     res = random.shuffle(list(resilt))
#     return ''.join(resilt)

# print(generate_random_string(57))
# print(generate_random_string(575))
# print(generate_random_string(517))
# print(generate_random_string(157))



# users = [
#   { 'name': 'Jack', 'age': 35, 'work': 'IT-backend developer' },
#   { 'name': 'Helen', 'age': 35, 'work': 'Nurse' },
#   { 'name': 'Bob', 'age': 35, 'work': 'Driver' },
#   { 'name': 'Jessica', 'age': 35, 'work': 'IT-frontend developer' },
#   { 'name': 'Helga', 'age': 35, 'work': 'IT-HR' }
# ]
# def func15(users):
#     ls = []
#     for dicts in users:
#         if 'IT' in str(dicts):
#             ls.append(f'{dicts["name"]}, скидки в магазине компьютерной техники!\n')
#     h = ''.join(ls)
#     return h
    


# print(func15(users))


# def func18(ls):
#     intls = []
#     strls = []
#     for item in ls:
#         if type(item) == str:
#             strls.append(item)
#         elif type(item) == int:
#             intls.append(item)
#     return strls, intls
# print(func18(['fxvxdvzd', 123, '124311', 'sefsfse', 3432]))









products = [
  {
    'title': 'Samsung S10', 
    'price': 800, 
    'count': 6, 
    'category': 'samsung'},
  {
    'title': 'iPhone 13 Pro', 
    'price': 1200, 
    'count': 9, 
    'category': 'apple'},
  {
    'title': 'Xiaomi Mi 10', 
    'price': 500, 
    'count': 2, 
    'category': 'xiaomi'},
  {
    'title': 'Samsung S9', 
    'price': 600, 
    'count': 4, 
    'category': 'samsung'},
  {
    'title': 'iPhone 11', 
    'price': 850, 
    'count': 1, 
    'category': 'apple'}
]
def func20(a:list,b:str)->list: 
    result=list() 
    for i in a: 
        if b.lower() in i['title'].lower(): 
            result.append(i) 
    return result

func20(products, 'i')