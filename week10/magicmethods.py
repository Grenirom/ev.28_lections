# magic methods (магические методы)
# dunder methods (double underscore) -> __init__
#Служебные методы

# Магия заключается в том, что эти методы запускаются без прямого обращения к ним, определенные методы могут отвечать за определенные операторы
 
# class A(int):
#     pass

# obj = A()
# print(dir(obj))

# Магические методы сравнения
# __eq__(self, other) -> 5 == 8

# __ne__ -> !=

# __lt__ -> <

# __gt__ -> >

# __le__ -> <=

# __ge__ -> >=

# print('15' < 'ABC')
# print(ord('1'), ord('A'))

# class Word(str):
#     def __new__(cls, obj):
#         # print(cls, '!!!')
#         # print(obj, "*****")
#         obj = obj.replace(' ', '')
#         return super().__new__(cls, obj)
    
    
#     def __gt__(self, other) -> bool:
#         print('gt Сработал!')
#         print(self, '***')
#         print(other)
#         # return len(self) > len(other) 
#         if len(self) > len(other):
#             return self
#         elif len(self) ==    
    
#     def __lt__(self, __value: str) -> bool:
#         return len(self) < len(__value)
    
#     def __eq__(self, __value: object) -> bool:
#         return len(self) == len(__value)
    


# obj = Word('  asc')
# obj1 = Word('    m oake rs')
# print(obj > obj1)
# print(obj < obj1)
# print(obj == obj1)
#----------------------------------------------------------------------
# + - / * // % **

# + -> __add__
# - -> __sub__
# * -> __mul__
# // -> __floordiv__
# / -> __truediv__
# % -> __mod__
# ** -> __pow__

# class Cifra:

#     def __new__(cls, *args, **kwargs):
#         number = abs(args[0])
#         instance = super().__new__(cls)
#         instance.number = number
#         return instance



#     def __add__(self, other):
#         print('add Была вызвана')
#         res = self.number + other.number
#         print(f'Result: {self.number} + {other.number} = {res}')
# value1 = Cifra(-117)
# v2 = Cifra(53)
# value1 + v2
#-----------------------------------------------------------------
# from random import choice

# class Dog:
#     def sound(self):
#         print('bark')

# class Cat:
#     def sound(self):
#         print('meow')

# class Lion:
#     def sound(self):
#         print('roar')

# class Pet:
#     def __new__(cls):
#         other = choice([Dog, Cat, Lion])
#         instance = super().__new__(other)
#         print(f'I\'m {type(instance).__name__}')
#         return instance

#     def __init__(self):
#         print('Pet was never called!')

# pet = Pet()
# pet.sound()
#---------------------------------------
# SINGLETON - Классы от которых можно создать только 1 экземпляр

# class Singleton:
#     _instance = None

#     def __new__(cls):
#         if not cls._instance:
#             cls._instance = super().__new__(cls)
#         return cls._instance
#     def __str__(self) -> str:
#         return str(id(self))
    
    
# a = Singleton()
# b = Singleton()
# print(a)
# print(b)
# print(a is b) #140385806547936
#               #140385806547936
#               #True   
# obj = Singleton()
# obj1 = Singleton()
# print(obj, obj1)
#-------------------------------------------------------------
# Дандер методы строкового отображения объектов
# # __str__
# # __repr__

# class Base:
#     def __init__(self, stroka):
#         self.string = stroka
#     #До объявления __str__ ->    <__main__.Base object at 0x7f172e898070>
#     def __str__(self) -> str:
#         return f'объект: {self.string}'
#     #объект: kase -> После

#     def __repr__(self) -> str:
#         return 'Base(\'Example\')'

# obj = Base('kase')
# print(obj)
# print(repr(obj))
# obj2 = Base('2Pac')
# print(obj2)
# print(repr(obj2))
# obj3 = eval(repr(obj2))
# print(obj3)
#------------------------------------------

# class Kopilka:
#     def __init__(self) -> None:
#         self.total = 0
#         self.coins = []

#     def add_coin(self, coin):
#         self.total += coin
#         self.coins.append(coin)

#     def __len__(self):
#         return len(self.coins)
    
#     def __getitem__(self, index):
#         return self.coins[index - 1]
    



# obj = Kopilka()
# obj.add_coin(12)
# obj.add_coin(2340)
# obj.add_coin(22)
# obj.add_coin(1532951)
# print(obj.total)
# print(obj.coins)
# print(len(obj))
# print(obj[1])