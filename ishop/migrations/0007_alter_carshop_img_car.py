# Generated by Django 3.2 on 2021-04-08 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ishop', '0006_alter_carshop_img_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carshop',
            name='img_car',
            field=models.ImageField(blank=True, default='default.png', upload_to='cars/', verbose_name='Картинка'),
        ),
    ]
