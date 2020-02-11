from django.db import models
from app.models.customer import Customer


class Payment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cost = models.IntegerField()
    vat = models.IntegerField()
    paid=models.IntegerField()
    date=models.DateField()
    class Meta:
        db_table = "payments"
