# синтаксис
# class SomeClass:
#     pass
#------------
# class A:
#     pass
# a = A() # Переменная 'a' - это объект/экземпляр от класса 'A'
# print(isinstance(a, A)) # метод проверяющий принадлежность объекта к классу. (сначала указывается в скобках объект, потом сам класс), возваращает буллевое значение

#----------------------------------
# class Dog:
#     # name = 'Rex' # name, age - атрибуты всего(свойства) класса
#     # age = 3
#     owner = 'John'

#     def __init__(self, name, age): # инициализатор, срабатывает всегда, даже без вызова
#         self.name = name
#         self.age = age

#     def bark(self):
#         print('Gav-Gav')

#     #@classmethod    #Декоратор который делает метод, методом всего класса
#     def eat(cks):
#         print('vkusno i tochka')

#     def __str__(self):
#         return f' {self.name} {self.age}'

#     def dog_info(self):
#         return f'This is {self.name}, he\'s {self.age} years old!'
    
#     def birthday(self, cake):
#         self.age += 1
#         self.cake = cake
#         # self.cake = 'Chocolate' # в методе можно создать новый атрибут экземпляра класса, и при вызове метода он автоматически появляется
#         print(f'У {self.name} сегодня день рождения! Ему теперь {self.age} лет!')

#     def friends(self, friend):
#         self.friend = friend
#         friend.friend = self


# dog1 = Dog(name='Bobik', age=2)
# dog2 = Dog(name='Rexi', age=5)
# dog1.friends(dog2)
# print(dog1.friend)
# print(dog2.friend.name)

# dog1.birthday('Chocolate')
# dog2.birthday('Milk Chocolate')
# print(dog1.age)
# print(dog1.cake) # Пример создания атрибута внуртри метода
# print(dog2.cake)
# dog1.bark()
# dog2.bark()
# dog3 = Dog(name='Oreo', age=1)
# dog3.owner = 'Alice'
# # print(dog1.owner)
# # print(dog3.owner)
# dog1.name = 'Booba' # переназначение атрибута экземпляра класса 
# dog1.food = 'Meat'
# print(dog1.name)
# print(dog1.food)  # создание нового атрибута экземпляра класса
# print(dog2.name)

#---------------------------------------------------
# class Rectangle:

#     default_color = 'red'

#     def __init__(self, width, length):
#         self.width = width
#         self.length = length
    
#     def area(self):
#         return self.width * self.length
    
    


# rec1 = Rectangle(4, 6)
# rec2 = Rectangle(2,7)
# rec2.default_color = 'Blue'
# print(rec2.default_color)
#---------------------------------------------
# class Car:
#     car_count = 0

#     def __init__(self):
        #------------------------------

                     #TASK1
# class Song:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year

#     def show_author(self):
#         return f'Название этой песни {self.title}'

#     def show_title(self):
#         return f'Автор этой песни {self.author}'

#     def show_year(self):
#         return f'Эта песня вышла в {self.year} году'

# song = Song('Yak2', 'Skryptonite', '2019')
# print(song.show_title())
# print(song.show_author())
# print(song.show_year())
#--------------------------------------------
#                           TASK2
# class Circle:
#     color = 'Синий'
#     pi = 3.14

#     def __init__(self, radius):
#         self.radius = radius
        

#     def get_area(self):
#         res = self.pi * (self.radius ** 2)
#         return res
    
# circle = Circle(2)
# circle.color = 'Yellow'
# print(circle.color)
# print(circle.get_area())
#---------------------------------------
#                   TASK 3
# class BankAccount:

#     def __init__(self):
#         self.balance = 0

#     def withdraw(self, amount):
#         self.amount = amount
#         self.balance -= self.amount
#         print(f'Ваш баланс: {self.balance} сом')
    
#     def deposit(self, amount):
#         self.amount = amount
#         self.balance += self.amount
#         print(f'Ваш баланс: {self.balance} сом')

# account = BankAccount()
# account.deposit(1000)
# account.withdraw(400)

#-------------------------------------------------------------------
#                   TASK 4
from typing import Any


# class Taxi:

#     def __init__(self, name, cost, cost_km):
#         self.name = name
#         self.cost = cost
#         self.cost_km = cost_km

#     def get_total_cost(self, km):
#         self.km = km
#         res = self.cost + (self.cost_km * self.km)
#         return f'Такси {self.name}, стоимость поездки: {res} сом'
    
# taxi1 = Taxi('Namba', 50, 10)
# taxi2 = Taxi('Yandex', 40, 12)
# taxi3 = Taxi('Jorgo', 70, 15)
# print(taxi1.get_total_cost(5))
# print(taxi2.get_total_cost(7))
# print(taxi3.get_total_cost(3))
#---------------------------------------------
#                   TASK 5
# class Phone:

#     def __init__(self, name, last_name, phone):
#         self.name = name
#         self.last_name = last_name
#         self.phone = phone

#     def get_info(self):
#         print(f'Контакт: {self.name} {self.last_name}, телефон: {self.phone}')
    
# contact = Phone('Nick', 'Grebnev', '+996707531295')
# contact.get_info()
#----------------------------------------------
#                       TASK 6
# class Salary:
#     percent = 8

#     def __init__(self, salary, experience):
#         self.salary = salary
#         self.experience = experience

#     def count_percent(self):
#         perc_p = (self.salary * self.percent) / 100
#         res = perc_p * self.experience
#         return res
    
# obj = Salary(10000, 10)
# print (obj.count_percent())
#----------------------------------
#                         TASK 7
# import datetime

# class Nobel:

#     def __init__(self, category, year, winner):
#         self.category = category
#         self.year = year
#         self.winner = winner

#     def get_year(self):
#         now = datetime.datetime.now()
#         data = now.year - self.year
#         print(f'{self.category} {self.year} {self.winner}')
#         print(f'выиграл {data} лет назад')
 
# winner1 = Nobel('Литература', 1971, 'Пабло Неруда')
# winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ")
# winner1.get_year()
# print(winner2.get_year())
# #------------------------------------------
#                   TASK 8
# digits = '1234567890'
# letters = 'abcdefghijklmnopqrstuvwxyz'
# symbols = '@', '#', '&', '$', '%', '!', '~', '*'

# class Password:
    
#     def __init__(self, password):
#         self.password = password
        
#     def validate(self):
#         if len(self.password) < 8 or len(self.password) > 15:
#             print('Password should be longer than 8, and less than 15')
#         try:
#             for i in self.password:
#                 if i in digits:
#         except:
#----------------------------------------------------------
#                   TASK 9 
from math import factorial


# a = '11'
# a = [int(digits) for digits in a]
# suma = sum(a)
# print(suma)

# class Math:

#     def __init__(self, number):
#         self.number = number

#     4def get_factorial(self):
#         return factorial(self.number)

#     def get_sum(self):
#         str_ = str(self.number)
#         str_ = [int(digit) for digit in str_]
#         suma = sum(str_)
#         return suma
    
#     def get_mul_table(self):
#         return '\n'.join([f"{self.number} x {i} = {self.number*i}" for i in range(1,11)]) 

    
# obj = Math(11)
# print(obj.get_factorial()) # работает
# print(obj.get_sum()) # работает
# print(obj.get_mul_table())
#-------------------------------

# class RadioMixin:

#     def play_music(self, title):
#         self.title = title
#         print(f'Песня называется {self.title}')
    
# class Auto(RadioMixin):
#     pass
# class Boat(RadioMixin):
#     pass
# class Amphibian(Auto, Boat):
#     pass

# auto = Auto()
# boat = Boat()
# obj = Amphibian()
# # auto.play_music()
# # boat.play_music()
# obj.play_music('YAk')
#-----------------------------
#               TASK 10

# class ToDo:
#     instances = {}

#     def __init__(self, to_do):
#         self.todo = to_do

#     def give_priority(self, priority):  #число по приоритету
#         self.priority = priority
#         self.instances.setdefault(self.priority, self.to_do)

#     def list_of_tasks(self):
#         res = sorted(self.instances.items(), key=lambda x: x[0])
#         return dict(res)

# var1=ToDo('ckelele') 
# var1.give_priority(2) 
# var2=ToDo('lelelele') 
# var2.give_priority(3) 
# var3=ToDo('HIOHOHO') 
# var3.give_priority(1)
# print(var1.list_of_tasks())
#--------------------------------------------
# class ToDo: 
#     def __init__(self,string): 
#         self.todo=string 
#     instances=dict() 
#     def give_priority(self,priority): 
#         ToDo.instances[priority]=self.todo 
#     def list_of_tasks(self): 
#         return sorted(ToDo.instances.items()) 
        
# var1=ToDo('ckelele') 
# var1.give_priority(2) 
# var2=ToDo('lelelele') 
# var2.give_priority(3) 
# var3=ToDo('HIOHOHO') 
# var3.give_priority(1) 
# print(var3.list_of_tasks())








# ar3=ToDo('HIOHOHO') var3.give_priority(1) print(var3.list_of_tasks())
# N




# class ContactList(list):
#     def __init__(self, list_):
#         self.list_ = list_

#     def search_by_name(self, name):
#         self.name = name
#         for x in self.list_:
#             res = []
#             # print(x)
#             if name == self.list_:
#                 res.append(self.name)
#             print(res)
# all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan'])
# print(all_contacts.search_by_name('Olya'))

# class Person:

#     def __init__(self):
#         self.__name = None
#         self.__last_name = None
#         self.__age = None
#         self.__email = None

#     def get_name(self):
#         gett = self.__name
#         return gett
#     def set_name(self, name):
#         self.__name = name
#         return name
    
#     def get_last_name(self):
#         get = self.__last_name
#         return get
    
#     def set_last_name(self, last_name):
#         self.__last_name = last_name
#         return last_name
    
#     def get_age(self):
#         gettt = self.__age
#         return gettt
    
#     def set_age(self, age):
#         self.__age = age
#         return age
    
#     def get_email(self):
#         get = self.__email
#         return get
    
#     def set_email(self, email):
#         self.__email = email
#         return email
    
    
# john = Person()
# # print(john.get_name()) # None
# # print(john.get_last_name()) # None
# # print(john.get_age()) # None
# # print(john.get_email())
# # print()
# john.set_name('John')
# john.set_last_name('Snow')
# john.set_age(30)
# john.set_email('johnsnow@gmail.com')
# print(john.get_name()) # John
# print(john.get_last_name()) # Snow
# print(john.get_age()) # 30
# print(john.get_email())
#-------------------------------
"""
ООП НАСЛЕДОВАНИЕ, САМОСТОЯТЕЛЬНОЕ ИЗУЧЕНИЕ
"""
#Функция: super() - возвращает все методы из родительского класса
# class Person:
#     test = 'Makers'

#     def __init__(self, name, last_name, id_number):
#         self.name = name
#         self.last_name = last_name
#         self.id_number = id_number

#     def get_info(self):
#         print(f'Name: {self.name}, Last Name: {self.last_name}, ID: {self.id_number}')
    
# class Employee(Person):
#     def __init__(self, name, last_name, id_number, position, salary):
#         super().__init__(name, last_name, id_number)
#         self.position = position
#         self.salary = salary

#     def get_info(self):
#         super().get_info()
#         # print(f'Name: {self.name}, Last Name: {self.last_name}, ID: {self.id_number}')
#         print(super().test)
#         print(f'He works as {self.position}, and his salary is {self.salary}')

# person = Person(name='John', last_name='Snow', id_number=234)
# person.get_info()


# employee = Employee(name='john', last_name='Snow', id_number=3422, position='It-Specialist', salary=100000)
# employee.get_info()
#-----------------------------------------------------
# class Art:
#     students_count = 100

# class Music(Art):
#     students_count = 50
#     def __init__(self):
#         Music.students_count += 1
#         Art.students_count += 1


# class Acting(Art):
#     students_count = 50
    
#     def __init__(self):
#         Acting.students_count += 1
#         Art.students_count += 1

# st1 = Music()
# st2 = Acting()
# st3 = Music()
# st4 = Acting()
# print(Music.students_count)
# print(Acting.students_count)
# print(Art.students_count)
"""
В этом примере нельзя использовать метод super(), выдаст ошибку, поэтому нужно отдельно к каждому классу обращаться
"""
#-------------------------------------------------------
# class Animal:
#     def sound(self):
#         raise NotImplementedError

# class Cat(Animal):
#     def sound(self):
#         print('Meow')

# class Dog(Animal):
#     def sound(self):
#         print('Gav-Gav')

# class Frog(Animal):

#     def sound(self):
#         print('Quack-Quack')

# an = Animal()
# # an.sound()
# cat = Cat()
# cat.sound()
# dog = Dog()
# dog.sound()
# frog = Frog()
# frog.sound()
#-----------------------------------------------------------
#                               TASKS:
#------------------------------------------------------------
#                               TASK 3
# class MyString(str):
#     def __init__(self, stroka1):
#         self.stroka1 = stroka1

#     def append(self, string2):
#         self.string2 = string2
#         res = self.stroka1 + self.string2 
#         return res

#     def pop(self):
#         last_w = self.stroka1[-1] 
#         self.stroka1 = self.stroka1[:-1] 
#         return last_w
    
#     def __str__(self) -> str:
#         return self.stroka1
    
# example = MyString('string')
# print(example.append('hello'))
# print(example)
# print(example.pop())
# print(example)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print(f'name: {self.name}, age: {self.age}')

# class Student(Person):
#     def __init__(self, name, age, faculty):
#         super().__init__(name, age)
#         self.faculty = faculty

#     def display_student(self):
#         print(f'name: {self.name}, age: {self.age}, faculty: {self.faculty}')

# obj_student = Student('Rick', 21, 'science')
# obj_student.display()
# obj_student.display_student()

# class ContactList(list):
#     def __init__(self, list_):
#         self.list_ = list_

#     def search_by_name(self, name):
#         a = []
#         for i in self.list_:
#             if name in i:
#                 a.append(i)
#         return a
# all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan'])
# print(all_contacts.search_by_name('Olya'))
#*----------------------------------
#                   TASK 7 
# from datetime import datetime

# class SmartPhones:
#     battery = 0

#     def __init__(self, name, color, memory):
#         self.name = name
#         self.color = color
#         self.memory = memory
        
#     def __str__(self) -> str:
#         return f'{self.name} {self.memory}'
    
#     def charge(self, amount):
#         self.amount = amount
#         self.battery += self.amount

# class Iphone(SmartPhones):
#     def __init__(self, name, color, memory, ios):
#         super().__init__(name, color, memory)
#         self.ios = ios

#     def send_imessage(self, stroka):
#         self.stroka = stroka
#         return f'sending {stroka} from {self.name} {self.memory}'
    
# class Samsung(SmartPhones):
#     def __init__(self, name, color, memory, android):
#         super().__init__(name, color, memory)
#         self.android = android

#     def show_time(self):
#         a = datetime.now().time()
#         return a

# phone = SmartPhones('generic', 'blue', '128GB')
# print(phone)
# print(phone.battery)
# phone.charge(20)
# print(phone.battery)
# iphone7 = Iphone('Iphone 7', 'Sierra-Blue', '128gb', 15.1)
# print(iphone7)
# print(iphone7.send_imessage('hello'))
# samsung21 = Samsung('Samsung-A21', 'Black', '128GB', 'Oreo')
# print(samsung21.show_time())
#-----------------------------
#                           TASK 8

# class CustomError(Exception): 
#     def __init__(self, message): 
#         self.message = message 
# capitals_error = CustomError('ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ')

# def check_letters(str_): 
#     if str_.islower(): 
#         raise capitals_error 
#     else: 
#         return f'ВСЕ ОТЛИЧНО! {str_}' 
# print(check_letters("HELLO")) 
# print(check_letters("hello"))
#---------------------------------------------------
#                       TASK 3
# class MyString(str): 
#     def append(self, extra_string): 
#         self.new_string = self + extra_string 
#     def pop(self): 
#         last_liter = self.new_string[-1] 
#         self.new_string = self.new_string[:-1] 
#         return last_liter 
#     def __str__(self): 
#         return self.new_string 

# example = MyString('String') 
# example.append('hello') 
# print(example)
# example.pop()
# print(example.pop())