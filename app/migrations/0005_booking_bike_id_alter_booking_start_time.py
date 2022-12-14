# Generated by Django 4.1.1 on 2022-11-05 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_booking_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='bike_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.bike'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
