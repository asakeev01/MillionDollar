from django.contrib import admin
from django.db.models.query_utils import Q

from .models import *


admin.site.register(Product)
admin.site.register(Meal)
admin.site.register(Weight)