# Generated by Django 3.1.7 on 2021-03-28 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AppCategory', '0002_auto_20210328_2221'),
        ('AppTags', '0002_auto_20210328_2221'),
        ('AppUsers', '0017_auto_20210328_2221'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('details', models.CharField(max_length=250)),
                ('actualDonation', models.IntegerField(default=0)),
                ('totalTarget', models.IntegerField()),
                ('startTime', models.DateTimeField()),
                ('endTime', models.DateTimeField()),
                ('rate', models.IntegerField(default=0)),
                ('NUN_users_make_rate', models.IntegerField(default=0)),
                ('NUN_users_make_Donate', models.IntegerField(default=0)),
                ('isSelect', models.BooleanField(default=False)),
                ('catID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppCategory.category')),
                ('userID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AppUsers.users')),
            ],
        ),
        migrations.CreateModel(
            name='projectImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgPath', models.ImageField(upload_to='images/project/')),
                ('projectID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppProject.projects')),
            ],
        ),
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentStr', models.TextField()),
                ('startTime', models.DateTimeField()),
                ('projectID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppProject.projects')),
                ('replay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppProject.comments')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppUsers.users')),
            ],
        ),
        migrations.CreateModel(
            name='tagProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppProject.projects')),
                ('tagID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppTags.tags')),
            ],
            options={
                'unique_together': {('tagID', 'projectID')},
            },
        ),
    ]
