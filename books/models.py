from django.db import models
from django.urls import reverse


class Publisher(models.Model):
    title = models.CharField(max_length=124)
    Address = models.CharField(max_length=124)

    def __str__(self):
        return self.title


class Author(models.Model):
    fullname = models.CharField(max_length=124)
    birthdate = models.DateTimeField()

    def __str__(self):
        return self.fullname


class Genre(models.Model):
    name = models.CharField(max_length=48)
    fiction = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=124)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField()
    quantity = models.IntegerField()
    self_cost = models.IntegerField()
    price = models.IntegerField()
    isbn = models.CharField(max_length=124)
    genre = models.ManyToManyField(Genre)
    pages = models.IntegerField()
    purchase_date = models.DateField()

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.title

    @staticmethod
    def get_absolute_url():
        return reverse('books')


class Warehouse(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class BooksInStore(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)


class Order(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    order_quantity = models.IntegerField()
    order_date = models.DateField(auto_now_add=True)
    order_receive = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['-pk']

    class Status(models.TextChoices):
        ORDERED = 'O'
        DONE = 'D'

    status = models.CharField(choices=Status.choices, max_length=12, default='O')

    def __str__(self):
        return f'{self.book} - {self.store}'

    @staticmethod
    def get_absolute_url():
        return reverse('orders')


class Sale(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    sales_quantity = models.IntegerField()
    sales_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.book} - {self.store}'
