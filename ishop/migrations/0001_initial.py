# Generated by Django 3.2 on 2021-04-08 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_car', models.CharField(choices=[('', 'Выберите марку'), ('hyundai', 'Hyundai'), ('chevrolet', 'Chevrolet'), ('renault', 'Renault')], default='', max_length=20, verbose_name='Марка')),
                ('title_car', models.CharField(max_length=50, verbose_name='Название')),
            ],
        ),
    ]