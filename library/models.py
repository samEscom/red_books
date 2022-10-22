from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    key_string = models.CharField(max_length=100)
    is_active = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ["-created"]

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    is_active = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'libros'
        ordering = ["-created"]

    def __str__(self):
        return self.name
