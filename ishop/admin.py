from django.contrib import admin
from .models import (
    CarShop,
    Currency,
)

# Register your models here.
admin.site.register(CarShop)
admin.site.register(Currency)