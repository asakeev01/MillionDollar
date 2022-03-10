from django.db import models


from apps.kitchen.models import *


class Order(models.Model):
    meals = models.ManyToManyField(Meal)
    openTime = models.DateTimeField(auto_now_add = True)
    closeTime = models.DateTimeField(null = True)
    opened = models.BooleanField(default = True)



