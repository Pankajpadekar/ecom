# Generated by Django 5.1 on 2024-08-21 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, default=' ', max_length=200, null=True),
        ),
    ]
