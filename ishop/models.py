from django.db import models

# Create your models here.
MODEL_CHOICES = [
    ('', "Выберите марку",),
    ('hyundai', 'Hyundai'),
    ('chevrolet', 'Chevrolet'),
    ('renault', 'Renault')
]

CURRENCY_CHOICES = [
    ('', "Выберите валюту",),
    ('WON', 'Wona'),
    ('USD', 'USDollars'),
    ('UZS', 'UzSum')
]

class Currency(models.Model):
    currency = models.CharField(verbose_name='Валюта', max_length=20, choices=CURRENCY_CHOICES, blank=True, default='')
    def __str__(self):
        return self.currency

class CarShop(models.Model):
    model_car = models.CharField(verbose_name='Марка', max_length=20, choices=MODEL_CHOICES, default='')
    title_car = models.CharField(verbose_name='Название', max_length=50)
    description_car = models.TextField(verbose_name="Описание", null=True, blank=True,)
    price_car = models.IntegerField(verbose_name="Цена", default=0)
    condition = models.CharField(verbose_name='Состояние', max_length=150, null=True, blank=True,)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, blank=True, default='')
    img_car = models.ImageField(verbose_name="Картинка", default='cars/default.png', upload_to='cars/', blank=True,)

    def __str__(self):
        return self.title_car
