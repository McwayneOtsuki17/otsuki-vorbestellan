# Generated by Django 3.2.6 on 2022-03-01 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vorbestellenapp', '0002_reservations_rooms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='room_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vorbestellenapp.rooms'),
        ),
    ]
