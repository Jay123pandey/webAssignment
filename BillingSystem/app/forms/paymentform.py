from django import forms
from app.models.payment import Payment


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"
