# Generated by Django 3.1.1 on 2021-04-10 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0006_seller_reg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seller_reg',
            old_name='user_id',
            new_name='seller_id',
        ),
    ]
