
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, User


# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        return redirect("list_books")
    else:
        return render(request, "books/homepage.html")

@login_required
def list_books(request):
    books = Book.objects.all().order_by("created_at")
    return render(request, "books/list_books.html",
    {"books": books})