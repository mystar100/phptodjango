# Generated by Django 4.2 on 2023-05-11 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_alter_invoice_date_alter_invoice_paydate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]