from django.db import models

# Create your models here.
class Vehicle(models.Model):
    id = models.AutoField(primary_key=True)
    reg_number = models.CharField(max_length=255)
    label = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return "Vehicle '%s', %s" % (self.reg_number, self.label)
