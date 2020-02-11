from django.db import models
from app.models.customer import Customer
from app.models.item import Item


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    class Meta:
        db_table = "orders"
