import datetime
from django.db import models
from django.contrib.auth.models import User
from vehicles.models import Vehicle

class Journey(models.Model):
    id = models.AutoField(primary_key=True)
    vehicle = models.ForeignKey(to=Vehicle, related_name='journeys', verbose_name="vehicle", on_delete=models.CASCADE)
    time = models.DateTimeField(default=datetime.datetime.now)
    length = models.DecimalField(max_digits=100, decimal_places=1)
    passengers = models.ManyToManyField(User, verbose_name=('users'), help_text=(""), through='JourneyPassengers')

    def __str__(self):
        return "Journey '%s', %s" % (self.vehicle.reg_number, self.time)

class JourneyPassengers(models.Model):
    id = models.AutoField(primary_key=True)
    journey = models.ForeignKey(Journey, null=True, blank=True, on_delete=models.CASCADE)
    passenger = models.ForeignKey(User, on_delete=models.CASCADE)

