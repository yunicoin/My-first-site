from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView


class UserMake(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'sigin.html'

class See(PermissionRequiredMixin, ListView):
    permission_required = 'auth.view_user'
    model = User
    template_name = 'indexUser.html'
