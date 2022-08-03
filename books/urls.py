from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('books/', BookListView.as_view(), name='books'),
    path('add_books/', BookCreateView.as_view(), name='add_book'),
    path('order/', OrderCreateView.as_view(), name='order'),
    path('orders/', OrderListView.as_view(), name='orders'),
    ]
