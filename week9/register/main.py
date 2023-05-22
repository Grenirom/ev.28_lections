from register import RegisterMixin, LoginMixin

class User(RegisterMixin, LoginMixin):
    pass

obj = User()
# print('Hello!')
# print('In our site you can register(1) or login(2) to existed user!')
# # choice = input('What you gonna do? 1 or 2').strip()

print(obj.register('TirionL', 'Tirion', 'Lanister', 'bastard123', 'bastard123'))
print(obj.login('TirionL', 'bastard123'))
