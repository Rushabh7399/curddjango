from django import forms
from django.forms import ModelForm
from Users.models import Orders

class UserForm(forms.Form):
    name = forms.CharField(label="Enter first name", max_length=50)
    age = forms.IntegerField(label="Enter Age")
    number = forms.CharField(label="Enter mobile number", max_length=10)
    birth_date = forms.DateField(label="Enter birth date")
    address = forms.CharField(label="Enter address", widget=forms.Textarea)

class OrderForm(ModelForm):
    class Meta:
        model = Orders
        fields = "__all__"

