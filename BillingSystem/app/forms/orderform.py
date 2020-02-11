from django import forms
from app.models.order import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
