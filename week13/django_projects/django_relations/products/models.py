from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=129)
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return f'{self.title}'


class Product(models.Model):
    title = models.CharField(max_length=130)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    amount = models.PositiveIntegerField(default=100)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.title
