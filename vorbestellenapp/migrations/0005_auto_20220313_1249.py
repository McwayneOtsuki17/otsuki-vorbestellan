# Generated by Django 3.2.6 on 2022-03-13 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vorbestellenapp', '0004_auto_20220313_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservations',
            name='date',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservations',
            name='reserver',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservations',
            name='reserver_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='vorbestellenapp.users', to_field='username'),
            preserve_default=False,
        ),
    ]
