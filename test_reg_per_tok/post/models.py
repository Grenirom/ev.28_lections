from django.db import models

from category_of_tech.models import Category


class Post(models.Model):
    title = models.CharField(max_length=150, required=True)
    image = models.ImageField(upload_to='images/', required=True)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='posts')
