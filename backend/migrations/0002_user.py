# Generated by Django 3.2.7 on 2022-03-27 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=100)),
                ('is_love', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=200)),
            ],
        ),
    ]
