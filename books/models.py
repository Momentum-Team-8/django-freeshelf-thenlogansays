from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    categories = models.ManyToManyField("Category", related_name="books")
    created_at = models.DateTimeField(default=timezone.now())

    def __repr__(self):
        return f"<Book title={self.title}>"

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50)

    def __repr__(self):
        return f"<Category name={self.name}>"

    def __str__(self):
        return self.name
