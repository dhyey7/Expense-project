# Generated by Django 4.1.7 on 2023-03-15 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Expense', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currencytype',
            old_name='currecy',
            new_name='Currency',
        ),
    ]
