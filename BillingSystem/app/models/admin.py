from django.db import models

class Admin(models.Model):
    User_Id= models.AutoField(auto_created=True,primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    class Meta:
        db_table="Admin"