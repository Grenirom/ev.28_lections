#1
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





















# #3
# class Bike:
#     def __init__(self, cost, make, model, year, condition):
#         self.cost = cost
#         self.make = make
#         self.model = model
#         self.year = year
#         self.condition = condition
#         self._sale_price = None
#         self.sold = False
#         self.min_gain = 5000

#     def set_sale_price(self, price):
#         if price < self.cost:
#             self._sale_price = self.cost + self.min_gain
#             return self._sale_price
#         else:
#             self._sale_price = price
#             return self._sale_price
    
#     def service(self, rep_cost, new_cond):
#         self._sale_price += rep_cost
#         self.condition = new_cond
#         return f'Price: {self._sale_price}, Condition: {self.condition}'
        
#     def sell(self):
#         self.sold = True
#         return f'You earned {self._sale_price} from this bike!'

#     def get_default_bike(self):
#         self.cost = 100000
#         self.make = 'CHINA'
#         self.model = 'ASI'
#         self.year = 2023
#         self.condition = 'Awesome'
#         self._sale_price = 120000
#         self.sold = False
#         self.min_gain = 5000


# bike = Bike(30000, 'USA', 'BH3', 2018, 'AWSM')
# print(bike.set_sale_price(40000))
# print(bike.service(3000, 'awssm++++'))
# print(bike.sold)
# print(bike.sell())
# print(bike.sold)
# print(bike.get_default_bike())


"""
4) Герой.
Разработайте программу по следующему описанию.
В некой игре-стратегии есть солдаты и герои. У всех есть свойство, содержащее
уникальный номер объекта, и свойство, в котором хранится принадлежность команде. У
солдат есть метод "иду за героем", который в качестве аргумента принимает объект типа
"герой". У героев есть метод увеличения собственного уровня.
В основной ветке программы создается по одному герою для каждой команды. В цикле
генерируются объекты-солдаты. Их принадлежность команде определяется случайно.
Солдаты разных команд добавляются в разные списки.
Измеряется длина списков солдат противоборствующих команд и выводится на экран. У
героя, принадлежащего команде с более длинным списком, поднимается уровень.
Отправьте одного из солдат первого героя следовать за ним. Выведите на экран
идентификационные номера этих двух юнитов.
"""

class Hero:
    