from django.views.generic.list import ListView
from django.views.generic import DetailView

from .models import Book


class BookList(ListView):
    model               = Book
    template_name       = 'books/book-list.html'
    context_object_name = 'books'


class BookDetail(DetailView):
    model               = Book
    template_name       = 'books/book-detail.html'
    context_object_name = 'book'
    slug_field          = 'isbn'
    slug_url_kwarg      = 'isbn'



