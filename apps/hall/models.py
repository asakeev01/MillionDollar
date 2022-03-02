from django.db import models

from apps.kitchen.models import *


class Order(models.Model):
    time = models.TimeField(auto_now_add= True)
    meals = models.ManyToManyField(Meal)
