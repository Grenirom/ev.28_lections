"""
Инкапсуляция:
1) Языковая конструкция, которая помогает связать данные с методами для их обработки и управления(связь между данными и методами, которые управляют ими) (класс - капсула)

2) Механизм сокрытия, при помощи которого можно ограничить доступ одного компонента программы к другому 
"""

# Инкапсуляция как связь

# class Phone:
#     number = '+996707531295'

#     def print_number(self):
#         print(f'Мой номер: {Phone.number}')
#         print(f'Мой номер: {self.number}')

# myPhone = Phone()
# myPhone.print_number()

#------------------------------------------------
# Инкапсуляция как механизм скорытия
# 3 уровня сокрытия данных в питоне:
#     1) Публичный(public) - number, print_number
#     2) Защищенный (_protected) - _number
#     3) Приватный(__private) - __number

# class Car:
#     _country = 'Germany'

#     def __init__(self) -> None:
#         self.marka = 'Mercedes-Benz' # public
#         self._model = 'e63' # protected
#         self.__color = 'Black'  #private
        
# obj = Car()
# print(dir(obj))
# print(obj._Car__color)
# print(obj._country)
# print(obj._model)
#----------------------------------------
# class Phone:
#     username = 'John'
#     _caller = 'Jamie'
#     __count_of_calls = 15

#     def call(self):
#         print(f'{self._caller} Звонит вам!')
#         question = input('взять трубку(yes/no):')
#         if question.lower().strip() == 'yes':
#             self.__turn_on()
#         else:
#             print('Сбросили трубку!')

        
#     def __increment_calls(self):
#         self.__count_of_calls += 1

#     def __turn_on(self):
#         self.__increment_calls()
#         print('Alo!')
#         print(f'Count of calls with {self._caller}: {self.__count_of_calls}')

# john = Phone()
# print(john.username)
# john.call()
#----------------------------------

# class Person:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def display_info(self):
#         print(f'My name is {self.name}, and i\'m {self.age} years old!')

# obj = Person('John', 18)
# obj.display_info()
# obj.nationality = 'Kyrgyz'
# # print(dir(obj))
# obj.age = -18
# obj.display_info()
#------------------------------------------------------
#getter & setter
# Они нужны чтобы избежать прямого обращения к сокрытым атрибутам, при этом можно добавить логику валидации(проверки) двнных которые будут установлены в атрибут

# class Person:
#     def __init__(self, name, age) -> None:
#         self.__name = name
#         self.__age = age

#     def display_info(self):
#         print(f'My name is {self.__name}, and i\'m {self.__age} years old!')
    

#     #getter
#     def name(self):
#         return self.__name
    
#     #setter
#     def set_age(self, age):
#         if not isinstance(age, int) or not 0 <= age < 150:
#             print('Invalid value for age!')
#         else:
#            self.__age = age

#     def set_name(self, name):
#         if not isinstance(name, str):
#             print('Invalid value for age!')
#         else:
#             self.__name = name



# obj = Person('John', 18)
# # print(obj.name())
# obj.set_age(-18)
# obj.display_info()
# obj.set_name('rick')
# obj.display_info()
#------------------------------------------

