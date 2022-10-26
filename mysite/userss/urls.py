from django.urls import path

from . import views

app_name = 'userss'
urlpatterns = [
    path('reg/', views.UserMake.as_view()),
],