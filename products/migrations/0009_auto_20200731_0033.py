# Generated by Django 2.2.10 on 2020-07-30 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
