# Generated by Django 5.1 on 2024-09-02 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_conf', '0002_rename_transaction_transaction_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction_item',
            name='processed',
            field=models.BooleanField(default=False),
        ),
    ]
