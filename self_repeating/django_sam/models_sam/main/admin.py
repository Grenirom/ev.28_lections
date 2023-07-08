
from django.contrib import admin

from main.models import Author, Genre, Book


admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Author)
