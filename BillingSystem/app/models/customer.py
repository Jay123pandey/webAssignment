from django.db import models


class Customer(models.Model):
    Customer_id = models.AutoField(auto_created=True, primary_key=True)
    Customer_name = models.CharField(max_length=200)
    Customer_address = models.CharField(max_length=200)

    class Meta:
        db_table = "customers"
