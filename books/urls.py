from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('books/', BookListView.as_view(), name='books'),
    path('add_books/', BookCreateView.as_view(), name='add_book'),
    path('order/', OrderCreateView.as_view(), name='order'),
    path('order_done/', order_done, name='order_done'),
    path('orders/', OrderListView.as_view(), name='orders'),
    path('sales/', SaleListView.as_view(), name='sales'),
    path('sale/', SaleCreateView.as_view(), name='sale'),

]
