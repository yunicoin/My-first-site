from django.urls import path

from . import views

app_name = 'userss'
urlpatterns = [
    path('bliks/', views.See.as_view()),
    path('reg/', views.UserMake.as_view()),
]