# Generated by Django 4.2.4 on 2023-12-12 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0008_alter_volunteerhour_time_in_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteerhour',
            name='time_in',
            field=models.TimeField(default='07:16:50'),
        ),
        migrations.AlterField(
            model_name='volunteerhour',
            name='time_out',
            field=models.TimeField(default='07:16:50'),
        ),
    ]