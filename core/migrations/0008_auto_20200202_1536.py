# Generated by Django 2.2 on 2020-02-02 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_cupon_valid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cupon',
            name='valid',
            field=models.BooleanField(default=True),
        ),
    ]
