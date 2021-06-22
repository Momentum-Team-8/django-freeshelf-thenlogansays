from django.shortcuts import render
from .models import Book


# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, "books/list_books.html",
    {"books": books})