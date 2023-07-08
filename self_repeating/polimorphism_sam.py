#                   TASK 2
# class Dog:

#     def voice(self):
#         print('Гав')

# class Cat:
#     def voice(self):
#         print('Мяу')
# barsik = Cat()
# rex = Dog()

# def to_pet(animal):
#     if isinstance(animal, Dog):
#         return animal.voice()
#     else:
#         return animal.voice()

# to_pet(barsik) 
# to_pet(rex) 
#------------------------------------------------
#                   TASK 3
# class Person:
#     def __init__(self, name, last_name):
#         self.name = name
#         self.last_name = last_name
#     def get_info(self):
#         return f'Привет, меня зовут {self.name} {self.last_name}'
# class Employee(Person):
#     def __init__(self, name, last_name, work, status):
#         super().__init__(name, last_name)
#         self.work = work
#         self.status = status
#     def get_info(self):
#         return f'Привет, меня зовут {self.name} {self.last_name}, я работаю в компании {self.work} на должности {self.status}'
# class Student(Person):
#     def __init__(self, name, last_name, university, course):
#         super().__init__(name, last_name)
#         self.university = university
#         self.course = course
#     def get_info(self):
#         return f'Привет, меня зовут {self.name} {self.last_name}, я учусь в {self.university} на {self.course} курсе'
# person = Person('Иван', 'Петров')    
# employee = Employee('Иван', 'Петров', 'Рога и копыта', 'директор')
# student = Student('Иван', 'Петров', 'КГТУ', 3)
# def get_human_info(human):
#     print(human.get_info())
# get_human_info(person)
# get_human_info(student)
# get_human_info(employee)
#-------------------------------------------------
#                       TASK 4
# from abc import ABC, abstractmethod 
# from math import pi

# class Shape:
#     @ABC
#     def get_area(self):
#         pass
# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#     def get_area(self):
#         return self.base * self.height * 0.5
# class Square(Shape):
#     def __init__(self, length):
#         self.length = length
#     def get_area(self):
#         return self.length ** 2
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def get_area(self):
#         return pi * self.radius ** 2
# triangle = Triangle(5, 5)
# square = Square(4)
# circle = Circle(3)

# print(triangle.get_area()) 
# print(square.get_area()) 
# print(circle.get_area()) 
#----------------------------------------------------------------
#                       TASK 5  
# class OS:
#     def __init__(self, version):
#         self.version = version
# class Windows(OS):
#     def copy(self, text):
#         # self.text = text
#         return f'скопирован текст "{text}" горячими клавишами CTRL + C'
# class MacOS(OS):
#     def copy(self, text):
#         return f'скопирован текст "{text}" горячими клавишами COMMAND + C'
# class Linux(OS):
#     def copy(self, text):
#         return f'скопирован текст "{text}" горячими клавишами CTRL + SHIFT + C'
# win = Windows(12)
# mac = MacOS(2)
# lin = Linux(1.12)
# print(win.copy("Полиморфизм — одна из основных парадигм ООП"))
# print(mac.copy("Полиморфизм - разное поведение одного и того же метода в разных классах"))
# print(lin.copy("На самом деле одинаковым является только имя метода, его исходный код зависит от класса"))
#----------------------------------------------------------------
#                           TASK 6
# class Language: 
#     def __init__(self, level, type) -> None: 
#         self.lvl = level 
#         self.type = type 
# class Python(Language): 
#     def write_function(self, func_name, arg): 
#         return f"def {func_name}({arg}):" 
#     def create_variable(self, var_name, value): 
#         if isinstance(value, str): 
#             return f"{var_name} = '{value}'" #
#         else: 
#             return f"{var_name} = {value}" 
# class JavaScript(Language): 
#     def write_function(self, func_name, arg): 
#         return f"function {func_name}({arg}) {{ }};" 
#     def create_variable(self, var_name, value): 
#         if isinstance(value, str): 
#             return f"let {var_name} = '{value}';" 
#         else: 
#             return f"let {var_name} = {value};" 
# py = Python('Intermediate', 'Backend') 
# print(py.write_function('get_code', 'a')) 
# print(py.create_variable('name', 'John')) 
# js = JavaScript('Advanced', 'Frontend') 
# print(js.write_function('validate', 'form')) 
# print(js.create_variable('password', 'john@123'))
#----------------------------------------------------------------
#                                  TASK 7
# class Money:
#     def __init__(self, country, symbol):
#         self.country = country
#         self.symbol = symbol
# class Dollar(Money):
#     rate =  84.80
#     def exchange(self, amount):
#         res = self.rate * amount
#         return f'$ {amount} равен {float(res)} сомам' 
# class Euro(Money):
#     rate = 98.40
#     def exchange(self, amount):
#         res = self.rate * amount
#         return f'€ {amount} равен {float(res)} сомам'
# dol = Dollar('USA', 'ANY')
# euro = Euro('SMC', 'asucon')
# print(dol.exchange(120))
# print(euro.exchange(120))
#++----------------------------------------------------------------
#                                 TASK 8
# class Planet:
#     def __init__(self, orbit):
#         self.orbit = orbit

# class Mercury(Planet):
#     # orbit = 88
#     def __init__(self, orbit):
#         self.orbit = orbit

#     def get_age(self, earth_age):
#         age = earth_age * 365 / self.orbit
#         return f'на Меркурии ваш возраст составляет {int(age)} лет'
# class Venus(Planet):
#     # orbit = 225
#     def __init__(self, orbit):
#         self.orbit = orbit
#     def get_age(self, earth_age):
#         age = (earth_age * 365 / self.orbit) * 365
#         return f'на Венере ваш возраст составляет {int(age)} дней'
# class Jupiter(Planet):
#     # orbit = 12
#     def __init__(self, orbit):
#         self.orbit = orbit
#     def get_age(self, earth_age):
#         age = earth_age * 365 // self.orbit * 365 * 24
#         return f'на Юпитере ваш возраст составляет {age} часов'
# mer = Mercury(88)
# ven = Venus(12)
# jup =Jupiter(12)
# print(ven.get_age(17))
# print(jup.get_age(30))
# print(mer.get_age(20))

# class Planet: 
#     def __init__(self, orbit): 
#         self.orbit = orbit 
# class Mercury(Planet): 
#     def get_age(self, earth_age): 
#         return f'на Меркурии ваш возраст составляет {int(earth_age * 365 /self.orbit)} лет' 
# class Venus(Planet): 
#     def get_age(self, earth_age): 
#         return f'на Венере ваш возраст составляет {round(earth_age * 365 / self.orbit * 365)} дней' 
# class Jupiter(Planet): 
#     def get_age(self, earth_age): 
#         return f'на Юпитере ваш возраст составляет {round(earth_age * 365 // self.orbit * 365 * 24)} часов' 
# mercury = Mercury(88) 
# venus = Venus(225) 
# jupiter = Jupiter(12)
# print(venus.get_age(20)) 
# print(jupiter.get_age(20)) 
# print(mercury.get_age(20))



class A:
    def __init__(self, s) -> None:
        self.s = s