#ООП - объектно ориентированное программирование

# Класс - это описание того, как должен выглядеть объект, то есть в классе мы описываем то, какими свойствами(данными) и поведением(функции) должен обладать объект

# Объект - это сущность, которую мы создаем от класса, у объекта есть собственные состояния свойств(данные)

# Целью создания, было связяать данные с функциями, которые управляли этими данными

# Свойства - это аттрибуты, называют обычные переменные внутри класса в которых хранятся данные объекта

# Методы - это обычные функции внутри класса, методы описывают поведение обЪекта
#-----------------------------------------------


# class Human:
#     age = 0
#     def __init__(self, first_name, last_name, job, citizenship):
#         self.name = first_name + ' ' + last_name
#         self.job = job
#         self.citizen = citizenship

#     def show_info(self):
#         return f'Name: {self.name}, Age: {self.age}, Job: {self.job}, Citizen: {self.citizen}'

# john = Human('John', 'Snow', 'King of North', 'Northerner')
# billal = Human('Billal', 'Lanister', 'Programmer', 'KR')

# print(john, type(john))
# print(dir(john))
# print(john.show_info())
# john.age = 24
# print(john.show_info())
# john.job = 'King of Wedteros'
# print(john.show_info)
# print(billal.show_info())
#---------------------------------------------------------------
# class Dog:
#     # Аттрибуты класса
#     age = 0
#     ears = True
    
#     def __init__(self, name, color) -> None:
#         "Инициализато, именно здесь создаются аттрибуты объекта"
#         # self - ссылка на объект который только что
#         self.name = name
#         self.color = color

#     def bark(self):
#         print(f'{self.name} лает!')
    
#     def show_info(self):
#         print(f'Name: {self.name}, Age: {self.age}, Color: {self.color}, Ears: {self.ears}')

# bobik = Dog('Bobik', 'Orange')
# rex = Dog(name='Rex', color='Black')
# pluto = Dog(name='Pluto', color='White')
# aktosh = Dog('Aktosh', 'Gray')

# # rex.show_info()
# # pluto.show_info()
# # bobik.show_info()
# # aktosh.show_info()

# rex.age = 2
# pluto.age = 5
# aktosh.age = 3
# aktosh.ears = False

# rex.show_info()
# pluto.show_info()
# bobik.show_info()
# aktosh.show_info()

# rex.bark()
# pluto.bark()
# bobik.bark()
#--------------------------------------------

# class Human():
#     def __init__(self):
#         print('init worked!')
#         self.raychel = 'raychel'
#         self.golod = 100

#     def eat(self, meal, doela=True):
#         print(f'{self.raychel} покушала {meal}')
#         if doela:
#             self.golod -= 50
#         else:
#             self.golod -= 25
# obj = Human()
# print(obj.raychel, obj.golod)
# obj.eat('burger', doela=False)
# print(obj.raychel, obj.golod)
# obj.eat('Kruasan')
# print(obj.raychel, obj.golod)
