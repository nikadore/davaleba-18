from django.shortcuts import render
from app.models import Book, Author, Genre


# # არაეფექტური კოდი (N+1 პრობლემა)
# books = Book.objects.all()

# for book in books:
#     print(f"Title: {book.title}, Author: {book.author}, Genre: {book.genre}")


# ოპტიმიზაცია
books = Book.objects.all().select_related('author').prefetch_related('genre')

for book in books:
    genres = ", ".join([genre.type for genre in book.genre.all()])
    print(f"Title: {book.title}, Author: {book.author.name}, Genres: {genres}")

