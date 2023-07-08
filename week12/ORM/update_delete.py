from models import Product, Category

# query = Product.update(price=1_000_000).where(Product.id==5)
# print(query, '!!!')
# query.execute()

# # query = Product.update(title='Airpods Pro').where(Product.title=='Hp')
# print(query, '!!!')
# query.execute

# query = Product.update(price=(Product.price * 1.5))
# query.execute() # Увеличиваем всем товарам цену


#-------------------------------------------------------
#Удаление данных

# product = Product.get(Product.id==2)
# print(product, product.title)
# product.delete_instance()
# print(product)

# query = Category.delete().where(Category.id==2)
# query.execute()