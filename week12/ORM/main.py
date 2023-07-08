# ORM (Object-Relational Mapping) - технология программирования, благодаря которой разработчики могут использовать язык программирования для взаимодействия с реляционной базой данных(PostgreSQL, MySQL и тд). Вместо того что-бы писать сырые запросы(Операторы SQL), вы будете писать код на языке программирования, это очень сильно ускоряет разработку приложения и бд, особенно на начальных этапах.


from peewee import PostgresqlDatabase, MySQLDatabase

db = PostgresqlDatabase(
    'orm_db',
    user='user',
    password='1',
    host='localhost', #127.0.0.1
    port=5432
)

# a = db.connect()
# print(a)