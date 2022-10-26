from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


class UserMake(CreateView):
    from_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'sigin.html'
