from django.db import models
from random import randint


class Category(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class PostImage(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='images/', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def create_image_name(self):
        return self.title + str(self.id) + str(randint(100000, 999999))

    def save_image(self, *args, **kwargs):
        self.title = self.create_image_name()
        return super(PostImage, self).save(*args, **kwargs)
