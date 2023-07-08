# Метод all() - возвращает все записи с определенной таблицы
#           ПРИМЕР:
#         Author.objects.all() - вернет все записи из таблицы Author
# ---------------------------------------------------------------------
# Метод filter() - фильтрует данные по определенному значению
#           ПРИМЕР:
#         Author.objects.filter(name='John') - выведет всех авторов по
#                                             имени 'John'
#           Author.objects.filter(name__startswith='J') - вернет все имена
# которые начинаются на букву 'J', для использования LookUpField'a (startswith, endswith, и тд.) используется 2 андерскора
# Вывод: <QuerySet [<Author: John Snow>, <Author: Joanne Rowling>, <Author: Jack London>]>

          # Author.objects.filter(name__endswith='e')  - <QuerySet [<Author: Joanne Rowling>]>
#-------------------------------------------------------------------------------------------------------------------

# Book.objects.filter(author__name='John Snow')
# Более сложный запрос, пытаемся вытащить все книги автором которых является "John Snow".
# для этого выбираем таблицу "Book", и в фильтре указываем поле "author", у которого внешний ключ от таблицы "Author"
# и поле "name"(которое из "Author"), через 2 андерскора, потому что "name" на данный момент является тоже неким
# лукапфилдом, соответственно и вызов такой
#                 <QuerySet [<Book: White Ship>, <Book: Call of the wild>]>
#                   Book.objects.filter(genre='Horror')
#                     <QuerySet [<Book: White Ship>, <Book: Call of the wild>]>
# genre является полем ManyToMany, поэтому необязательно через 2 андерскора обращаться к таблице Genre, и вытягивать оттуда slug
# он является PrimaryKey
#----------------------------------------------------------------------------------------------------------------------
# exclude() - метод, работающий так-же как и filter(), но если filter() возвращал все, что соответствовало условию
# то exclude() возвращает все, что не соответствует.
#             Book.objects.exclude(genre='Horror')
#             <QuerySet [<Book: Harry Potter and Philosopher's stone>]> - книга, жанр которой не хоррор

            #  Book.objects.exclude(title__contains='Harry')
            # <QuerySet [<Book: White Ship>, <Book: Call of the wild>]>
# contains - содержит, в этом запросе просим вывести все книги которые не содержат в себе слово "Harry"
# contains чувствителен к регистру, чтобы он стал нечувствительным нужно вначале поставить 'i'
#                                                                             icontains
#                                         Book.objects.filter(title__icontains='HARRY')
#                                         <QuerySet [<Book: Harry Potter and Philosopher's stone>]>

#-----------------------------------------------------------------------------------------------------

# order_by() - метод сортировки
#             Author.objects.order_by('date_of_birth') -
#             <QuerySet [<Author: Jack London>, <Author: Joanne Rowling>, <Author: John Snow>]> - от меньшего к большему

#              Author.objects.order_by('-date_of_birth')
#              <QuerySet [<Author: Jack London>, <Author: Joanne Rowling>, <Author: John Snow>]> от большего к меньшему
#------------------------------------------------------------
#Еще можно комбининровать методы(сцеплять), например:
# Book.objects.filter(genre='Horror').order_by('title')
# <QuerySet [<Book: Call of the wild>, <Book: White Ship>]>
#--------------------------------------------------------
#annotate() - метод принимающий агрегационные функции (avg, count, min, max и тд.)
#  queryset = Book.objects.annotate(Count('genre'))
#  queryset
# <QuerySet [<Book: Harry Potter and Philosopher's stone>, <Book: White Ship>, <Book: Call of the wild>]>
# ВЫВОДИТ ВСЕ КНИГИ, И АВТОМАТИЧЕСКИ СОЗДАЕТ ПОЛЕ КОТОРОЕ ВЫСЧИТЫВАЕТ КОЛИЧЕСТВО КНИГ (ИЗНАЧАЛЬНО МЫ ЕГО НЕ СОЗДАВАЛИ)

# book = queryset[1] # БЕРЕМ КНИГУ, ОБРАЩАЯСЬ ПО ИНДЕКСУ
# book
# <Book: White Ship>
# book.genre__count #ПЕРЕМЕННАЯ В КОТОРОЙ КНИГА, ТОЧКА, ПОЛЕ КОТОРОЕ УКАЗЫВАЛИ, В НАШЕМ СЛУЧАЕ genre, и агрегационная
# функция которая вызывается через 2 андерскора
2 # количество жанров к которым относится эта книга
#                  |
# book.genre.all()
# <QuerySet [<Genre: Ужасы>, <Genre: Роман>]>
#----------------------------------------------------------------
# count() - высчитывает количество объектов в нашем queryset'e

# Author.objects.count()
# >>>3
# Genre.objects.count()
# >>>5
#-------------------------------------------------------
# exists() - метод, возвращающий True/False. В зависимости от того, существует ли определенная запись

# >>> Author.objects.filter(last_name__iendswith='ow').exists()
# True

# >>> Author.objects.filter(last_name__iendswith='ov').exists()
# False
#---------------------------------------------------------------------
# get() - метод, возращающий какой-либо полученный объект и только в единичном экземпляре. Возвращает объект, не QuerySet. Итерироваться не получится

# >>> Author.objects.get(name='John')
# <Author: John Snow>
#------------------------------------------------------------------------
# create() - метод создающий запись

#---------------------------------------------------------------
# first() - метод, который возвращает первую запись/первый объект
# >>> Author.objects.first()
# <Author: John Snow>
#
# last() - метод, который возвращает последнюю запись/объект
# >>> Author.objects.last()
# <Author: Jack London>
#------------------------------------------------
#             LookUpFields
# gt() - greater than
# >>> Author.objects.filter(date_of_birth__gt='1900-01-01')
# <QuerySet [<Author: John Snow>, <Author: Joanne Rowling>]>  - Авторы, которые родились позже 1900 года
# lt() - less than
# >>> Author.objects.filter(date_of_birth__lt='1900-01-01')
# <QuerySet [<Author: Jack London>]>
#-----------------------------------------------------


# related_name='<your related name>' - это имя, с помощью которого можно обратиться ко всем объектам модели

#                       |
# >>> Author.objects.get(id=2)
# <Author: Joanne Rowling>
# >>> author = Author.objects.get(id=2)
# >>> author
# <Author: Joanne Rowling>
# >>> author.books.all()
# <QuerySet [<Book: Harry Potter and Philosopher's stone>]>
