# Generated by Django 4.0.5 on 2022-07-13 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_jobdetails_comdetaile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gettouch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('subject', models.CharField(max_length=250)),
                ('message', models.CharField(max_length=1500)),
            ],
        ),
    ]