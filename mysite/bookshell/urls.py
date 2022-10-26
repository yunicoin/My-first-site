from django.urls import path

from . import views
app_name = 'books'
urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list_book, name='lists'),
    path('book/<int:book_id>/', views.read, name='book_info'),
    path('book/make/', views.BookMake.as_view()),
]