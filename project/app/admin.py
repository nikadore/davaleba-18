from django.contrib import admin
from app.models import Book, Author, Genre

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)