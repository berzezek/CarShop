# Generated by Django 3.2 on 2021-04-08 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ishop', '0003_alter_currency_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='currency',
            field=models.CharField(blank=True, choices=[('', 'Выберите валюту'), ('WON', 'Wona'), ('USD', 'USDollars'), ('UZS', 'UzSum')], default='', max_length=20, verbose_name='Валюта'),
        ),
    ]
