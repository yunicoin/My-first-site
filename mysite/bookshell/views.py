from django.contrib.auth.mixins import PermissionRequiredMixin, AccessMixin, LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView

from .models import Book


# Create your views here.

def index(request):
    return render(request, 'main.html')


def list_book(request):
    blist = Book.objects.order_by('-date')
    BL = []
    for i in blist:
        if i.accept:
            BL.append(i)
    return render(request, 'index.html', {'books':BL})

class BookMake(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['name', 'athor', 'date', 'text']
    template_name = 'Book_form.html'

def read(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if book.accept:
        return render(request, 'detail.html', {'book': book})
    return get_object_or_404(Book, pk=-1)
