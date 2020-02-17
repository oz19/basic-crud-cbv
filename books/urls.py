from django.urls import path

from .views import BookList, BookDetail


urlpatterns = [
    path('', BookList.as_view(), name='book-list'),
    path('<int:isbn>/', BookDetail.as_view(), name='book-detail'),
]
