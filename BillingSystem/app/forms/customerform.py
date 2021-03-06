from django import forms
from app.models.customer import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
