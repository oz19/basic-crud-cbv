from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

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


class AddBook(CreateView):
    model               = Book
    template_name       = 'books/add-book.html'
    fields              = ['name', 'isbn']
    success_url         = reverse_lazy('book-list')


class EditBook(UpdateView):
    model               = Book
    template_name       = 'books/edit-book.html'
    fields              = ['name', 'isbn']
    success_url         = reverse_lazy('book-list')
    slug_field          = 'isbn'
    slug_url_kwarg      = 'isbn'

class DeleteBook(DeleteView):
    model               = Book
    success_url         = reverse_lazy('book-list')
    slug_field          = 'isbn'
    slug_url_kwarg      = 'isbn'
    template_name       = 'books/delete-confirmation.html'

class DeleteConfirmation(TemplateView):
    template_name       = 'books/delete-confirmation.html'
    context_object_name = 'book'
