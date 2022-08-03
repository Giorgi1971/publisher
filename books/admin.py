from django.contrib import admin
from .models import Book, Publisher, Store, Warehouse, Order, Sale, Author, Genre


admin.site.register([Book, Publisher, Store, Warehouse, Order, Sale, Author, Genre])
