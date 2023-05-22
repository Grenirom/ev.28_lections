# from abc import ABC, abstractmethod

# class Coder(ABC):
#     count_code_time = 0
#     @abstractmethod
#     def get_info(self):
#         ...
#     @abstractmethod
#     def coding(self):
#         ...
# class Backend(Coder):
#     def __init__(self, experience, languages_backend):
#         self.experience = experience
#         self.languages_backend = languages_backend

#     def get_info(self):
#         return f'{self.languages_backend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часовна программирование'
#     def coding(self, val):
#         self.count_code_time = val

# class Frontend(Coder):
#     def __init__(self, experience, languages_frontend):
#         self.experience = experience
#         self.languages_frontend = languages_frontend

#     def get_info(self):
#         return f'{self.languages_frontend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часовна программирование'
#     def coding(self, val):
#         self.count_code_time = val
# class Fullstack(Backend, Frontend):
#     pass
# a = Backend('Junior', 'Python')
# b = Frontend('Middle', 'JavaScript')
# c = Fullstack('Senior', 'Python and JS')
# a.coding(12) 
# b.coding(45) 
# c.coding(17) 
# print(a.get_info()) 
# print(b.get_info()) 
# print(c.get_info()) 
#----------------------------------------------------------
#                   TASK 5
class Square:
    def __init__(self, side):
        self.side = side
    def get_area(self):
        return self.side ** 2
class Triangle:
    def __init__(self, height, base):
        self.height = height
        self.base = base
    def get_area(self):
        return (self.base * self.height) / 2
class Pyramid(Triangle, Square):
    def __init__(self, height, base):
        super().__init__(height, base)

    def get_volume(self):
        return int((1/3) * self.base ** 2 * self.height)
obj = Square(3)
print(obj.get_area())
obj1 = Triangle(16, 6)
print(obj1.get_area())
obj2 = Pyramid(16, 8)
print(obj2.get_volume())

