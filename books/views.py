from django.http import HttpResponseRedirect
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


def order_done(request):
    if request.method == 'POST':
        print(request.POST)
        order = Order.objects.get(pk=request.POST['q'])
        print(order)
        book = Book.objects.get(isbn__exact=order.book.isbn)
        book.quantity -= order.order_quantity
        print(book)
        book.save()
        order.status = 'D'
        order.save()
        print(order.status)
    return HttpResponseRedirect(reverse('orders'))
