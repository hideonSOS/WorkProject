from django.db import models

# Create your models here.
class test_database1(models.Model):
    id = models.AutoField(primary_key=True)
    str_area1 = models.CharField(max_length=10)
    str_area2 = models.CharField(max_length=100)
    date_field=models.DateField()

