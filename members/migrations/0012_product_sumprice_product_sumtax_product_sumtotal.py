# Generated by Django 4.2 on 2023-05-12 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0011_product1'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sumprice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='sumtax',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='sumtotal',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
    ]
