# Generated by Django 2.2.10 on 2020-08-02 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='sub_total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
    ]