from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .forms import *
from .models import Book, Order
from django.contrib import messages


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
        order = Order.objects.get(pk=request.POST['q'])
        if order.status == 'D':
            messages.add_message(request, messages.WARNING, 'This order already DONE!')
            return HttpResponseRedirect(reverse('orders'))

        book = Book.objects.get(isbn__exact=order.book.isbn)
        if book.quantity - order.order_quantity < 0:
            messages.add_message(request, messages.INFO, f'only {book.quantity} books stayed')
            return HttpResponseRedirect(reverse('orders'))
        book.quantity -= order.order_quantity
        book.save()
        order.status = 'D'
        order.save()
    return HttpResponseRedirect(reverse('orders'))
