# Generated by Django 3.2 on 2021-04-08 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ishop', '0008_auto_20210408_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carshop',
            name='condition',
            field=models.CharField(max_length=150, null=True, verbose_name='Состояние'),
        ),
    ]