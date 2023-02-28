from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=250)
    dob = models.DateField(auto_now=True)
    # age = models.IntegerField()
    gender = models.CharField(max_length=250)
    mob = models.IntegerField()
    mail = models.CharField(max_length=250)
    address = models.CharField(max_length=500)
    branch = models.CharField(max_length=250)
    district = models.CharField(max_length=250)
    actype = models.CharField(max_length=250)
    mp = models.CharField(max_length=250)

    def __str__(self):
        return self.name