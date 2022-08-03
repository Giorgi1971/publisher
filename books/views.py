from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .forms import *
from .models import Book, Order


def home(request):
    return render(request, 'home.html')


class BookListView(ListView):
    model = Book


class BookCreateView(CreateView):
    model = Book
    form_class = BookModelForm


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderModelForm


class OrderListView(ListView):
    model = Order
    fields = '__all__'
