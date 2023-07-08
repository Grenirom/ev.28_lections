# #Функция полиморфизм -> len(): __len__
# # print(len('makers'))
# # print(len([1,2,3,4])) 
# # print(len({1:2, 3:4}))

# # + (__add__) - метод полиморфизм

# # print(5 + 5)
# # print('hello' + 'hello')
# # print([1,2,3] + [4,5,6])
# #---------------------------------------------------
# """
# Полиморфизм - способность функции(метода) использоваться для разных типов(классов)

# Широко распространенное определение: "один интерфейс - Много реализаций"
# """
# # list.pop
# # set.pop
# # dict.pop
# #--------------------------
# # class Cat:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age

# #     def info(self):
# #         print(f'It\'s a cat! Cat\'s name is {self.name}, and it\'s age: {self.age}')

# #     def make_sound(self):
# #         print('Meow-Meow')
# # class Dog:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age

# #     def info(self):
# #         print(f'It\'s a Dog! Dog\'s name is {self.name}, and it\'s age: {self.age}')

# #     def make_sound(self):
# #         print('Gav-gav')


# # cat = Cat('Garfield', 8)
# # dog = Dog('Pluto', 3)

# # for obj in (cat, dog):
# #     obj.info()
# #     obj.make_sound()
# #-------------------------------
# from math import pi
# class Shape:
#     def __init__(self, name):
#         self.name = name

#     def area(self):
#         pass

#     def fact(self):
#         return f'Я фигур в двумерной плоскости: {self.name}!'
    

# class Square(Shape):
#     def __init__(self, length):
#         super().__init__('Квадрат')
#         self.length = length

#     def area(self):
#         return self.length ** 2
    
#     def fact(self):
#         return super().fact() + '\nУ квадрата все стороны равны и углы равны 90 градусам!'
    
# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__('Окружность')
#         self.radius = radius

#     def area(self):
#         return pi * (self.radius ** 2)
    
# a = Square(8)
# b = Circle(3)

# print(a.fact())
# print(a.area())
# print()
# print(b.fact())
# print(b.area())

class English:
    def greeting(self):
        print ("Hello")

class French:
    def greeting(self):
        print ("Bonjour")

    def intro(language):
        language.greeting()

john = English()
gerard = French()
gerard.intro()