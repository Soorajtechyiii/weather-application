from django.db import models #type:ignore
class Read(models.Model):
    countrycode=models.CharField(max_length=200,null=True)
    coordinate=models.CharField(max_length=200,null=True)
    temp=models.IntegerField(default=0)
    humidity=models.IntegerField(default=0)
def __str__(self):
    return self.countrycode,self.coordinate,self.temp,self.humidity


