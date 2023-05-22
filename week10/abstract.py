"""
Абстракция
"""
# Абстракция (Абстрактный класс) - принцип ООП, в котором создается абстрактный класс (класс - пустышка), в котором задаются названия атрибутов и методов, для того чотбы мы могли их переопределить в дочерних методах. (у нас есть название, но нет логики)

from abc import ABC, abstractmethod, abstractproperty

# class AbstractAnimal(ABC):

#     @abstractmethod
#     def voice(self):
#         ...

#     @abstractproperty
#     def legs(self):
#         ...
# # Создать объект от этого класса невозможно

# # class Dog(AbstractAnimal):
# #     ...
# # obj = Dog()
# #TypeError: Can't instantiate abstract class Dog with abstract methods legs, voice

# class Dog(AbstractAnimal):
#     legs = 4
#     def voice(self):
#         print('Gav-Gav!')

# #@abstractmethod - декоратор который требует переопределение метода в наследуемом классе
# #@abstractproperty - декоратор который требует переопределения аттрибутов класса


# obj = Dog() 
# obj.voice()
# print(obj.legs)
# #-------------------------------------------------------------
# class Shape(ABC):
#     def __init__(self, name):
#         self.name = name

#     @abstractmethod
#     def area(self):
#         ...

# class Square(Shape):
#     def __init__(self, length):
#         super().__init__('Square')
#         self.length = length

#     def area(self):
#         return self.length ** 2
# obj = Square(12)
# print(obj.area())
#---------------------------------------------------------------------
# class AbstractAnimal(ABC):

#     @abstractmethod
#     def voice(self):
#         ...

#     @abstractproperty
#     def legs(self):
#         ...

# class Dog(AbstractAnimal):
#     legs = 4
#     def voice(self):
#         print('Gav-Gav!')

# class Cat(AbstractAnimal):
#     legs = 4

#     def voice(self):
#         print('meow')
# dog = Dog()
# cat = Cat()
# arr = [dog, cat]
# for i in arr:
#     i.voice()
#     print(i.legs)
#------------------------------------------------------------------------------------

#                                       TASKS

#2)
"""
2) Создайте 3 класса:
Bird, Animal, Plant
класс Bird должен иметь методы: fly(), grow(), sound(). Animal: sound(), run(), grow(). Plant: grow(), photosynthesize()
каждый метод должен просто принтить действие. Например: def fly(self): print('я лечу')
!!!!
Обязательное условие: использовать абстракцию. Если не переопределить общий метод должна выходить ошибка
!!!!!
"""

# class AbstractAnimal(ABC):

#     @abstractmethod
#     def grow(self):
#         ...
# class Bird(AbstractAnimal):
#     def fly(self):
#         print('Я лечу!')

#     def grow(self):
#         print('Я расту!')

#     def sound(self):
#         print('чик-чирик')
# class Animal(AbstractAnimal):
    
#     def sound(self):
#         print('я звучу')

#     def run(self):
#         print("я бегу")

#     def grow(self):
#         print('я вырос')

# class Plant(AbstractAnimal):

#     def grow(self):
#         print('Я буду расти')
        
    
#     def photosynthesize(self):
#         print('just hit some')

# bird = Bird()
# bird.grow()
# print()
# animal = Animal()
# animal.grow()
# print()
# plant = Plant()
# plant.grow()
#------------------------------

# class Planet(ABC):
#     def __init__(self, orbit):
#         self.orbit = orbit
#     @abstractmethod
#     def get_age(self):
#         ...
# class Mercury(Planet):

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
#----------------------------------------------------
"""
1)Создайте два класса A и B. В обоих классах есть метод count. В классе A он подсчитывает, сколько гласных букв в слове, которое передается в качестве аргумента в методе count, а в классе B он подсчитывает количество согласных. Создайте объекты от этих классов. С помощью list comprehension создайте список из результатов работы метода count обоих объектов.

!!!! 
Обязательное условие: если в классе A или B не переопределить метод count должна выйти ошибка
!!!!

"""
class Abstracted(ABC):
    
    @abstractmethod
    def count(self):
        ...

class A(Abstracted):
    glas = ['а,я,у,ю,о,е,ё,э,и,ы']
    count_w = 0

    def count(self, string: str):
        self.string = string
        for i in string:
            if i in self.glas:
                self.count_w += 1
                print(self.count_w)
            
obj = A()
print(obj.count('привет'))
