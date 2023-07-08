import peewee
from models import Category, Product
import random


def add_category(name):
    try:
        obj = Category(title=name.lower().strip())
        obj.save()
        print(f'Сохранили категорию {obj} - {obj.title}')
    except (peewee.IntegrityError, peewee.InternalError):
        print(f'{name.lower().strip()} Эта категория уже существует!')

# add_category('SmartPhones')
add_category('SmartPhones')
add_category('Tv')
add_category('Laptops')
add_category('sony playstation')

def add_products(name, price, category_name):
    category_name = category_name.lower().strip()
    try:
        category = Category.get(title=category_name.lower().strip())
        print(category, category.title, category.created_at, '!!!!!')
    except peewee.DoesNotExist:
        price(f'Категории {category_name} не существует!')
    else:
        obj = Product(title=name, price=price, category_id = category)
        obj.save()
        print(f'Сохранили товар {obj} - {obj.title}')

# add_products('Sony PLayStation 5', 500, 'sony playstation')
# add_products('Hp', 660, 'laptops')
# add_products('Iphone 14 pro max', 1250, 'SmartPhones')
# add_products('Iphone 13 pro', 1000, 'SmartPhones')
# # add_products('Beats Solo 3', 150, 'Headphones')
# add_products('macbook pro m2', 3000, 'laptops')
#-----------------------------------------
# add_category('cars')

# with open('ORM/files/cars.txt', 'r') as file:
#     ls = file.readlines()
#     print(ls)
#     for x in ls:
#         name = x.strip()
#         price = random.randint(5000, 20000)
#         add_products(name, price, 'cars')

# with open('ORM/files/telefon.txt', 'r') as file:
#     ls = file.readlines()
#     print(ls)
#     for x in ls:
#         name = x.strip()
#         price = random.randint(200, 1300)
#         add_products(name, price, 'smartphones')
