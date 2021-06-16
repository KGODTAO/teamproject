from django.contrib import admin
from django.contrib.auth import get_user_model

from main.models import Book, Genre, Author,Comment

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Comment)

# Register your models here.
