# Generated by Django 5.1 on 2024-08-21 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('roll', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('image', models.CharField(max_length=100)),
            ],
        ),
    ]
