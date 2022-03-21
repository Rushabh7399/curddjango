from django.db import models


# Create your models here.
class Employee5(models.Model):
    emp_name = models.CharField(max_length = 50)
    emp_email = models.CharField(max_length = 50)
    emp_number = models.CharField(max_length = 50)

    class Meta:
        db_table = "Employee5"


