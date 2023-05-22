# class Human:
#     age = 0

#     def __init__(self, first_name, last_name, weight, nation):
#         self.name = f'{first_name} {last_name}'
#         self.weight = weight
#         self.nationality = nation

#     def birthday(self):
#         from random import randint
#         print(f'\nHappy Birthday, {self.name}!!!')
#         self.age += 1
#         self.weight += randint(3,7)

#     def show_info(self):
#         print(self.name, self.age, self.weight, self.nationality)
        



# human1 = Human('John', 'Snow', 3.300, 'American')
# human2 = Human('Abu', 'Al-Nassr', 3.8, 'Arab')

# human1.show_info()
# human2.show_info()
# print()
# print('After 1 year')
# human1.birthday()
# human2.birthday()

# human1.show_info()
# human2.show_info()

# human1.birthday()
# human2.birthday()
# human1.birthday()
# human2.birthday()
# human2.birthday()
# human2.birthday()

# human1.show_info()
# human2.show_info()
#--------------------------------------------------------------

# class Students:
#     univer = 'Harvard University'

#     def __init__(self, name):
#         self.name = name
#         self.books = []
#         self.languages = {}
#         self.knowledge = 0
#         self.is_ready_to_work = False

#     def add_points(self, points):
#         self.knowledge += points
#         if self.knowledge > 500 and not self.is_ready_to_work:
#             self.is_ready_to_work = True
#             print(f'{self.name} just hit 500 points!')
    
#     def read_book(self, book_name):
#         self.books.append(book_name)
#         self.add_points(50)

#     def do_project(self):
#         self.add_points(100)

#     def learn_new_lang(self, language, percent):
#         if percent not in range(70, 101):
#             print('Not enough points!')
#         else:
#             self.languages[language] = percent
#             self.add_points(percent)

# st1 = Students('John Snow')
# st2 = Students('Billal Billalovich')
# st3 = Students('Aizirek Akimbaeva')

# print(st1.name)
# print(st2.name)
# print(st3.name)

# print(f'Before study {st1.name}: {st1.books}, {st1.languages}, {st1.knowledge}')
# print(f'Ready to work: {st1.is_ready_to_work}')

# st1.read_book('Game of Thrones')
# st1.read_book('Martin Eden')
# st1.read_book('Algorithms and Data Structures')
# st1.read_book('Eugene Onegin')

# st1.do_project()
# st1.do_project()

# st1.learn_new_lang('Python', 40)
# st1.learn_new_lang('Python', 90)

# st1.learn_new_lang('C++', 75)

# st1.do_project()

# print(f'After the study {st1.name}: {st1.books}, {st1.languages}, {st1.knowledge}')
# print(f'Ready to work: {st1.is_ready_to_work}')
#---------------------------------------------------------
# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def show_info(self):
#         return f'{self.brand} -> {self.model}'
    
#     def __str__(self) -> str:
#         return f'{self.brand} -> {self.model}'

# obj = Car('BMW', 'M8 Competition')
# obj2 = Car('BMW', 'M5 f90')
# print(obj)
# print(obj2)

# print(obj.show_info())
#----------------------------------------------------------------------
# import random
# class Sniper:
#     health = 100

#     def __init__(self, name):
#         self.name = name
    
#     def get_shot(self, other):
#         other.health -= 20
#         print(f'Стрелял {self}')
#         print(f'У {other} осталось: {other.health}')

#     def __str__(self):
#         return self.name
    
# sniper1 = Sniper('John Snow')
# sniper2 = Sniper('Fridrih Sholtch')

# while sniper1.health and sniper2.health:
#     choice = random.randint(1,2)
#     sniper1.get_shot(sniper2) if choice == 1 else sniper2.get_shot(sniper1)

# if sniper1.health:
#     print(f'{sniper1} Won the Game!')
# else:
#     print(f'{sniper2} Won the Game!')  
#---------------------------------------------------------------------------
# class Soda:
#     def __init__(self, ingredient=None):
#         if isinstance(ingredient, str):
#             self.ingredient = ingredient
#         else:
#             self.ingredient = None

#     def __str__(self):
#         if self.ingredient:
#             return f'Soda is made of {self.ingredient}'
#         else:
#             return 'Normal Soda'

# a = Soda('Malina')
# print(a)
# b = Soda(5)
# print(b)
# c = Soda()
# print(c)

# d = Soda('Taurine')
# print(d)
#------------------------------------------------------
# from typing import List
# class Triangle_checker:
#     def __init__(self, sides: List[int or float]) -> None:
#         self.sides = sides

#     def __str__(self) -> str:
#         if not all(isinstance(x, (int, float)) for x in self.sides):
#             return 'Нельзя'
#         elif any(x <= 0 for x in self.sides):
#             return 'Нельзя'
#         self.sides.sort()
#         if self.sides[0] + self.sides[1] <= self.sides[-1]:
#             return 'Нельзя! сумма меньше или равна'
#         return 'Мы можем построить треугольник!'
        
# t1 = Triangle_checker([10, 10, 10])
# print(t1)
# print()
# t2 = Triangle_checker([-1, 10, 10])
# print(t2)
# print()
# t3 = Triangle_checker([5, 10, 12])
# print(t3)
# t4 = Triangle_checker([1, 6, 2])
# print(t4)