from views import CreateMixin, ReadMixin, UpdateMixin, DeleteMixin
import json


class Product(CreateMixin, ReadMixin, UpdateMixin, DeleteMixin):
    def save(self):
        with open('data.json', 'w') as file:
            json.dump(self.objects, file, indent=4)
            return "Saved!"

class Comment(CreateMixin, ReadMixin, DeleteMixin):
    pass

smartphones = Product()
print(smartphones.post(title='Redmi Note 10', description='The best phone for it\'s own price', qty=10, price=250))
print(smartphones.post(title='Redmi Note 30', description='The best phone!', qty=6, price=740))
print(smartphones.post(title='Iphone 14 Pro Max', description='The most expensive one', qty=100, price=1250))
print(smartphones.post(title='samsung S23', description='one of the best ones!', qty=1, price=1050))
print(smartphones.post(title='Iphone 13 pro', description='The fastest one!', qty=210, price=1000))
print()
print()
print(smartphones.list())
print()

print(smartphones.detail(4))
print(smartphones.detail(1))
print(smartphones.patch(1, title='Redmi Note 9'))
print()
print(smartphones.list())
print(smartphones.detail(1))
print()
print(smartphones.delete(-1))
print(smartphones.delete(1))
print(smartphones.save())
