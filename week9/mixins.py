# mixins
# Миксины - это классы которые используются для наследования и передачи дочерним классам определенных методов, но от них не создаются объекты

# для чего:
# 1. вы хотите предоставить множество дополнительных методов для классов 
# 2. вы хотите использовать один конкретный метод во множестве разных классов

# class EngineMixin:
#     def startEngine(self):
#         print('Started engine!')

# class RadioMixin:
#     def play_radio(self):
#         print('music is playing!')

# class Auto(EngineMixin, RadioMixin):
#     pass

# class Plane(EngineMixin):
#     pass

# class SmartPhone(RadioMixin):
#     pass

# class Train(EngineMixin, RadioMixin):
#     pass
#----------------------------------------------------------------------

# class FlyMixin:
#     def fly(self):
#         print('I can fly!')
    
# class WalkMixin:
#     def walk(self):
#         print('I can walk!')

# class SwimMixin:
#     def swim(self):
#         print('I can Swim!')

    
# class Human(WalkMixin, SwimMixin):
#     name = 'human'

#     def talk():
#         print('I can talk!')

# class Fish(SwimMixin):
#     name = 'fish'

# class Exocoetidae(SwimMixin, FlyMixin):
#     name = 'flying fish'

# class Duck(SwimMixin, WalkMixin, FlyMixin):
#     name = 'duck'

# obj = Human()
# obj.walk()
# obj.swim()# I can walk!
# # I can Swim!
#----------------------------------------------------------------------------

