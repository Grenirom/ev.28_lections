# Множественное наследование - это когда класс наследуется от 2-х и более классов


# class Auto:
#     def play_music_at_station(self):
#         print('Music is playing!')

#     def ride(self):
#         print('We\'re riding on the ground!')
    
# class Plane:
#     def play_music_at_station(self):
#         print('Listening Ed Sheeran!')

#     def fly(self):
#         print('We\'re flying!')

# class FutureAuto(Auto, Plane):  # множественное наследование, прсто передаем по очереди, через запятую
#     pass

# obj = FutureAuto()
# obj.ride()
# obj.fly()
# obj.play_music_at_station()
# obj.play_music_at_station()
# # print(dir(obj))
# # print(type(object))
#---------------
"""
Проблема ромба - когда поиск шел в родительский класс, прежде чем искать у соседнего общего потомка (решена с помощью MRO)
MRO (Method Resolution Order) - механзм для поиска родительских методов. Был создан для решения проблемы ромба, которая появилась после введения object в Python. Поиск идет таким образом, что если у родительских классов есть общий предок, то поиск идет в ширину
"""


# class Zero:
#     def say(self):
#         print('class Zero')

# class First(Zero):
#     def say(self):
#         print('class First')

# class Second(Zero):
#     def say(self):
#         print('class Second')

# class MyClass(First, Second):
#     def say(self):
#         super().say()
#         print('class MyClass')


# obj = MyClass()
# obj.say()
# print(MyClass.mro())
#-------------------------------------
# class Z: # 3
#     pass

# class Y: # 5
#     pass

# class A(Z): #2
#     pass

# class B(Y): # 4
#     pass
# class X(A, B): #1
#     pass

# print(X.mro())
#--------------------------------------
# Проблеиа перекрестного наследования

# class Y:
#     pass

# class X:
#     pass

# class A(X, Y): 
#     pass

# class B(Y, X):
#     pass

# class MyMro(type):
#     def mro(cls):
#         return [cls, A, B, X, Y, object]

# class MyClass(A, B, metaclass=MyMro):
#     pass

# print(MyClass.mro())
#---------------------------------
