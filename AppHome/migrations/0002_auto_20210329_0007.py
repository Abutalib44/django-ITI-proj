# Generated by Django 3.1.7 on 2021-03-28 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AppHome', '0001_initial'),
        ('AppProject', '0001_initial'),
        ('AppUsers', '0017_auto_20210328_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='projectID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppProject.projects'),
        ),
        migrations.AddField(
            model_name='donation',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppUsers.users'),
        ),
    ]
