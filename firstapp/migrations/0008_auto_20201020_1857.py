# Generated by Django 3.0.8 on 2020-10-20 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0007_auto_20201020_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(blank=True, default=False, max_length=254),
        ),
    ]
