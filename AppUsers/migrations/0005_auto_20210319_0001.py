# Generated by Django 3.1.7 on 2021-03-18 22:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppUsers', '0004_auto_20210318_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user',
            field=models.OneToOneField( blank=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
