# Generated by Django 5.0.6 on 2024-06-20 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_rename_variation_cartitem_variations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
