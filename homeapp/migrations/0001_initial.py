# Generated by Django 3.1.1 on 2021-01-10 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_reg',
            fields=[
                ('u_id', models.AutoField(primary_key=True, serialize=False)),
                ('u_name', models.CharField(max_length=200)),
                ('u_address', models.CharField(max_length=200)),
                ('u_phone', models.IntegerField(max_length=11)),
                ('u_pincode', models.CharField(max_length=6)),
            ],
        ),
    ]
