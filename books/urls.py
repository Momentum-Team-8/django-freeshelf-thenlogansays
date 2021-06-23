from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.homepage, name='home'),
    path("accounts/", include('registration.backends.simple.urls')),
    path("list/", views.list_books, name='list_books'),
]