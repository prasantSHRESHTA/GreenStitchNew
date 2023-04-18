from django.db import models

# Create your models here.

class category(models.Model):
    subject = models.CharField(max_length=100, null=False,blank=False)
    num_value = models.CharField(max_length=100, null=False,blank=False)
    percent_inc_dec = models.FloatField(null =False, blank = False)
    janValue = models.IntegerField(null =False, blank = False)
    febValue = models.IntegerField(null =False, blank = False)
    marValue = models.IntegerField(null =False, blank = False)
    aprValue = models.IntegerField(null =False, blank = False)
    mayValue = models.IntegerField(null =False, blank = False)
    juneValue = models.IntegerField(null =False, blank = False)
    julyValue = models.IntegerField(null =False, blank = False)
    top_emission = models.FloatField(null =False, blank = False)
    color = models.CharField(max_length=10)
    def __str__(self):
        return self.subject