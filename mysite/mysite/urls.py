from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    path('bookshell/', include('bookshell.urls')),
    path('admin/', admin.site.urls),
    path('mirror/', include('django.contrib.auth.urls'), name='login'),
    path('mirror/', include('userss.urls'))
],
