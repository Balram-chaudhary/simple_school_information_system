# Generated by Django 5.1 on 2024-08-21 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0003_rename_roll_teacher_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='phone',
            field=models.IntegerField(max_length=10),
        ),
    ]
