"""
Ассоциация - принцип в ООП, в котором два класса связаны друг с другом.Связь обозначает то, что внутри одного объекта будет существовать другой объект от другого класса
Агрегация - слабая ссвязь
Композиция - сильная связь
"""

# class Battery:
#     _power = 100

#     def charge(self):
#         if self._power < 100:
#             self._power = 100

# class Iphone:
#     def __init__(self, color):
#         self.color = color
#         self.battery = Battery()
#         #когда мы создаем внутри класса объект от другого класса, это - Композиция

# a = Iphone('gold')
# a.battery._power -= 50
# print(a.battery._power)
# a.battery.charge()
# print(a.battery._power)
# del a
# # При удалении Iphone, вместе с ним удаляется и батарейка

# class Nokia:
#     def __init__(self, battery: Battery, color: str):
#         self.color = color
#         self.battery = battery
#         #когда объект создается из вне класса и передается внутрь, это - Агрегарция

# battery = Battery()
# nokia1 = Nokia(battery, 'silver')
# print(nokia1.battery._power)
# del nokia1

# nokia2 = Nokia(battery, 'Black')
# #При удалении nokia, батарейка остается
#-----------------------------------------------
# Композиция

# class Wall:
#     def __init__(self, direction):
#         self.type = direction

#     def __str__(self) -> str:
#         return f'{self.type}'
    
# class Room:
#     def __init__(self):
#         self.west_wall = Wall('west')
#         self.east_wall = Wall('east')
#         self.south_wall = Wall('south')
#         self.north_wall = Wall('north')
# obj = Room()
# print(obj.west_wall)
# print(obj.east_wall)

#-----------------------
#Агрегация

# class Stream:
#     def __str__(self):
#         return 'Stream object'
    
# class Logger:
#     def __init__(self, stream=None):
#         self.stream = stream

#     def print_the_logs(self):
#         if self.stream:
#             print(f'Stream from class: {self.stream}')
#         else:
#             print('None stream!')



# stream1 = Stream()
# logger = Logger(stream1)
# logger2 = Logger(stream1)
# logger3 = Logger(stream=Stream())

# logger.print_the_logs()
# logger2.print_the_logs()
# logger3.print_the_logs()
#---------------------------------------------
class Engine:
    country = 'Germany'

    def __init__(self, power):
        self.power = power

    def __str__(self) -> str:
        return f'Power: {self.power}'
    
class AudiCar:
    brand = 'Audi'
    country = 'Germany'

    def __init__(self, model, power):
        self.engine = Engine(power)
        self.model = model
    
    def __str__(self) -> str:
        return f'{self.brand} {self.model} -> Engine: {self.engine} -> engine country: {self.engine.country}'
    
car = AudiCar('A8', 400)
print(car)