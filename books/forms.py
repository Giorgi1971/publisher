from django import forms
from .models import *
from django.forms.widgets import (
    TextInput, DateInput, SelectDateWidget, NumberInput, SelectMultiple, Select,
    CheckboxSelectMultiple, CheckboxInput, Input,
)


class OrderModelForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('store', 'book', 'order_quantity')


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'isbn': TextInput(attrs={'class': 'form-control', 'placeholder': 'ISBN'}),
            'rating': NumberInput(attrs={'class': 'form-control'}),
            'authors': SelectMultiple(attrs={'class': 'form-control'}),
            'publisher': Select(attrs={'class': 'form-control'}),
            'pubdate': DateInput(attrs={'class': 'form-control'}),
            'quantity': NumberInput(attrs={'class': 'form-control'}),
            'self_cost': NumberInput(attrs={'class': 'form-control'}),
            'price': NumberInput(attrs={'class': 'form-control'}),
            'pages': NumberInput(attrs={'class': 'form-control'}),
            'genre': SelectMultiple(attrs={'class': 'form-control'}),
            'purchase_date': SelectDateWidget(attrs={'class': 'form-control'}),
        }

        # def __init__(self, *args, **kwargs):
        #     super(BookModelForm, self).__init__(*args, **kwargs)
        #     for field in self.fields:
        #         self.fields[field].widget.attrs.update({'class': 'form-control'})
