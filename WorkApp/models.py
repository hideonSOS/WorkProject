from django.db import models

# Create your models here.
class test_database1(models.Model):
    id = models.AutoField(primary_key=True)
    str_area1 = models.CharField(max_length=10)
    str_area2 = models.CharField(max_length=100)
    date_field=models.DateField()

class test_database2(models.Model):
    idon = models.AutoField(primary_key=True)
    str_areaon1 = models.CharField(max_length=10)
    str_areaon2 = models.CharField(max_length=100)
    date_fieldon=models.DateField()

class Series(models.Model):
    id= models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    Syusai = models.CharField(max_length=5)
    start_day=models.DateField()
    end_day=models.DasteField()    end_day=models.DasteField()    end_day=models.DasteField()    end_day=models.DateField()