from django.db import models


# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    number = models.CharField(max_length=10)
    birth_date = models.DateField()
    address = models.TextField()


    class Meta:
        db_table = "users"


class Orders(models.Model):
    item_name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    order_total = models.IntegerField()
    hotel_Main_Img = models.ImageField(upload_to='images/', default=1)

    class Meta:
        db_table = "orders"
