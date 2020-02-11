from django import forms
from app.models.item import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"
