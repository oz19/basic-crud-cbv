from django.urls import path

from .views import (
    BookList,
    BookDetail,
    AddBook,
    EditBook,
    DeleteBook,
    DeleteConfirmation
)


urlpatterns = [
    path('', BookList.as_view(), name='book-list'),
    path('<int:isbn>/', BookDetail.as_view(), name='book-detail'),
    path('add/', AddBook.as_view(), name='add-book'),
    path('edit/<int:isbn>/', EditBook.as_view(), name='edit-book'),
    path('delete-confirmation/<int:isbn>/', DeleteConfirmation.as_view(), name='delete-confirmation'),
    path('delete/<int:isbn>/', DeleteBook.as_view(), name='delete-book'),
]
