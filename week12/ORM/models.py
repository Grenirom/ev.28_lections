import peewee
from main import db
from datetime import datetime
from playhouse.migrate import migrate, PostgresqlMigrator


class Category(peewee.Model):
    id = peewee.PrimaryKeyField()
    title = peewee.CharField(max_length=20, unique=True)
    created_at = peewee.DateTimeField(default=datetime.now())

    class Meta:
        database = db
        db_table = 'category'
        order_by = ('created_at',)

class Product(peewee.Model):
    id = peewee.PrimaryKeyField()
    title = peewee.CharField(max_length=40)
    price = peewee.DecimalField(max_digits=10, decimal_places=2, default=100)
    category_id = peewee.ForeignKeyField(Category, to_field='id',related_name='products')
    created_at = peewee.DateTimeField(default=datetime.now())

    class Meta:
        database = db
        db_table = 'product'
        order_by = ('Created_at')

db.connect()
# Category.create_table()
# Product.create_table()
#--------------------------------------------------------------
#migrate = изменение бд
# migrator = PostgresqlMigrator(db)
# migrate(
#     migrator.alter_column_type('product', 'title', peewee.TextField())
# )