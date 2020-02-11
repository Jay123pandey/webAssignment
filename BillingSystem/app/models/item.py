from django.db import models


class Item(models.Model):
    item_id = models.AutoField(auto_created=True, primary_key=True)
    item_name = models.CharField(max_length=200)
    item_image = models.ImageField()

    class Meta:
        db_table = "items"
