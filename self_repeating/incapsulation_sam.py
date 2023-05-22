"""
getter & setter
"""

# class User:
#     def __init__(self, name, password) -> None:
#         self.name = name
#         self.__password = password

#     #getter
#     def get_password(self, user):
#         if self.name == user:
#             return self.__password
#         else:
#             return "Entrance was not allowed!"
#     #setter
#     def set_password(self, old_password, new_password):
#         if self.__password == old_password:
#             self.__password = new_password
#             return 'Successfully changed'
#         else:
#             return 'You\'re not able to change the password!'
        

#     def __get_info(self):
#         print(f'Name: {self.name}, Password: {self.__password}')

# user1 = User('John', '12344lasd')
# print(user1.get_password('John'))
# print(user1.set_password('12344lasd', 'ask;cm'))
#-------------------------------------------------
# class Divider:
#     def __init__(self) -> None:
#         self.__divide_num = 1
    
#     @property   # getter
#     def divider(self):
#         return self.__divide_num
    
#     @divider.setter # В Setter, перед точкой надо указать название метода
#     def divider(self, value):
#         if not value == 0:
#             self.__divide_num = value
#             return self.__divide_num
#         else:
#             return 'No!'

#     def divide(self, value):
#         return self.__divide_num / value
# obj = Divider()
# obj.divider = 22
# print(obj.get_divider)
"""
Декоратор @property позволяет обращаться к методу как к свойству, или к атрибуту объекта этого класса
"""

# class Person:
#     def __init__(self, name, last_name):
#         self.name = name
#         self.last_name = last_name
          
#     @property
#     def full_name(self):
#         return f'{self.name} {self.last_name}'
    

# obj = Person('John', "Snow")
# print(obj.full_name)




































#----------------------------------------------------------------------------
#                           TASK 3
# class Car:
#     __speed = 0
#     @property
#     def speed(self):
#         return self.__speed
    
#     @speed.setter
#     def speed(self, val):
#         self.__speed = val
# car1 = Car()
# print(car1.show_speed())
# car1.set_speed(20)
# print(car1.show_speed())
#-------------------------------------------------------
#                   TASK 5
# class Person:
    # name = "John"
    # _phone_number = "+996 557 55 17 57"
    # __card_number = "9999 9999 9999 9999"

# john = Person()
# print(john.name)
# print(john._phone_number)
# print(john._Person__card_number)
#-------------------------------------------------------------------
#                       TASK 6
# class Person:
#     def __init__(self, name, phone_number, card_number):
#         self.name = name
#         self._phone_number = phone_number
#         self.__card_number = card_number



# john = Person("John", "+996 557 55 17 57",  "9999 9999 9999 9999")
# print(john.name)
# print(john._phone_number)
# print(john._Person__card_number)
#----------------------------------------------------------
#                   TASK 7
# class Person:

#     _phone_number = "+996 557 55 17 57"
#     __card_number = "9999 9999 9999 9999"

# john = Person()
# john.name = None
# john._phone_number = None
# john._Person__card_number = None
# print(john.name)
# print(john._phone_number)
# print(john._Person__card_number)
#-----------------------------------------------------------------
#                   TASK 8 
# class Person:
#     def __init__(self, name, phone_number, card_number):
#         self.name = self.__validate_name(name) 
#         self._phone_number = phone_number
#         self.__card_number = card_number
#     def __validate_name(self, name):
#         if len(name) < 2:
#             self.name = "John"
#             return self.name
#         else:
#             return name.capitalize()
    
#     def get_number(self):
#         return self._phone_number
#     def get_card_number(self):
#         return self.__card_number
    

    
# sam = Person("SAM", "+996 557 55 17 57", "9999 9999 9999 9999")
# print(sam.name)
# print(type(sam.get_number()))
# print(type(sam.get_card_number()))
#-----------------------------------------------------------------------
#                       TASK 9
# class Person:
#     def __init__(self, name, phone_number, card_number):
#         self.name = name
#         self._phone_number = self._validate_phone_number(phone_number)
#         self.__card_number = self.__validate_card_number(card_number)

#     def _validate_phone_number(self, phone_number):
#         if isinstance(phone_number, int) and str(phone_number).startswith('996'):
#             return phone_number
#         return None
#     def __validate_card_number(self, card_number):
#         if isinstance(card_number, int) and len(str(card_number)) == 16:
#             return card_number
#         return None
        
        
# tolik = Person('Tolik', 996707531295, 9999999999999999)
# print(tolik.name)
# print(tolik._phone_number)
# print(tolik._Person__card_number)
#---------------------------------------------------------
#               TASK 10
# class Game:
#     __level = 0
#     def __init__(self, name):
#         self.name = name

#     def play(self, hours):
#         if hours > 2:
#             self.__level += 1
    
#     def get_level(self):
#         return self.__level
    
# game = Game('John')
# print(game.get_level())
# print(game.play(3))
# print(game.play(3))
# print(game.get_level())
#-------------------------------------------------------------
#               TASK 11
 
# class Game: 
#     __level = 0 
#     def __init__(self, name): 
#         self.name = self.__validate_name(name) 
#     def set_level(self, level): 
#         if self.name == 'Tolik': 
#             self.__level = level 
#         else: 
#             print(f"{self.name} ты не Tolik!") 
#     def __validate_name(self, name): 
#         return name.title() 
# game = Game('Raychel') 
# game.set_level(5) 
# print(game._Game__level) 
# game2 = Game('TOLIK') 
# game2.set_level(5) 
# print(game2._Game__level)
#-----------------------------------------------------
#                   TASK 12
# class Game:
#     __level = 0

#     def __init__(self, name):
#         self.name = name

#     def get_level(self):
#         return self.__level
    
#     def set_level(self, lvl):
#         self.__level = lvl
# game = Game('John')
# print(game.get_level())
# game.set_level(10)
# print(game.get_level())
#----------------------------------------
#               TASK13
# class Game:
#     __level = 0

#     @property
#     def level(self):
#         return self.__level
# game = Game()
# print(game.level)
#-------------------------------------------------
#           TASK 14
# class Game:
#     __level = 0

#     @property
#     def level(self):
#         return self.__level
    
#     @level.setter
#     def level(self, value):
#         self.__level = value
# game = Game()
# print(game.level)
# game.level = 10
# print(game.level)
#-------------------------------------------------
#               TASK15
# class Person:

#     def __init__(self):
#         self.__name = None
#         self.__last_name = None
#         self.__age = None
#         self.__email = None
#     def get_name(self):
#         return self.__name
#     def set_name(self, val):
#         self.__name = val
#     def get_last_name(self):
#         return self.__last_name 
    
#     def set_last_name(self, val):
#         self.__last_name = val

#     def get_age(self):
#         return self.__age
    
#     def set_age(self, val):
#         self.__age = val

#     def get_email(self):
#         return self.__email
    
#     def set_email(self, val):
#         self.__email = val
# john = Person()
# print(john.get_name()) # None
# print(john.get_last_name()) # None
# print(john.get_age()) # None
# print(john.get_email()) # None
# john.set_name('John')
# john.set_last_name('Snow')
# john.set_age(30)
# john.set_email('johnsnow@gmail.com')
# print(john.get_name()) # John
# print(john.get_last_name()) # Snow
# print(john.get_age()) # 30
# print(john.get_email()) # johnsnow@gmail.com
#-----------------------------------------------------
#                   TASK 16
# class Person:

#     def __init__(self):
#         self.__name = None
#         self.__last_name = None
#         self.__age = None
#         self.__email = None

#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self, val):
#         self.__name = val

#     @property
#     def last_name(self):
#         return self.__last_name
#     @last_name.setter
#     def last_name(self, val):
#         self.__last_name = val
    
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self, val):
#         self.__age = val
    
#     @property
#     def email(self):
#         return self.__email
#     @email.setter
#     def email(self, val):
#         self.__email = val
# john = Person()
# print(john.name) # None
# print(john.last_name) # None
# print(john.age) # None
# print(john.email) # None
# john.name = 'John'
# john.last_name = 'Snow'
# john.age = 30
# john.email = 'johnsnow@gmail.com'
# print(john.name) # John
# print(john.last_name) # Snow
# print(john.age) # 30
# print(john.email) # johnsnow@gmail.com
#-------------------------------------------
#              TASK 17
# class Dad:
#     name = 'John'
#     _last_name = 'Snow'
#     __age = 40
# class Me(Dad):
#     name = 'Sam'
#     __age = 10

#     def about_me(self):
#         print(f'My name is {self.name} {self._last_name} and I am {self._Me__age} years old')
#     def about_dad(self):
#         print(f'My father is {Dad.name} {Dad._last_name}')
# me = Me()
# me.about_me()
# me.about_dad()