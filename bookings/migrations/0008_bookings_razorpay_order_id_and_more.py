# Generated by Django 4.1.7 on 2023-03-14 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0007_alter_bookings_listing_id_alter_bookings_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='razorpay_order_id',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='bookings',
            name='razorpay_payment_id',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='bookings',
            name='razorpay_signature',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
