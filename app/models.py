from django.db import models

# Create your models here.
class Country(models.Model):
    cname=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.cname

class Capital(models.Model):
    cname=models.OneToOneField(Country,on_delete=models.CASCADE)
    cappop=models.IntegerField()
    capname=models.CharField(max_length=100,primary_key=True)
