# Generated by Django 4.1.7 on 2023-03-12 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='listing_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='user_id',
            field=models.IntegerField(null=True),
        ),
    ]
