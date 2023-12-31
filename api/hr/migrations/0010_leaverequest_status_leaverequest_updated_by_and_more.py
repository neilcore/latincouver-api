# Generated by Django 4.2.4 on 2023-12-19 08:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hr', '0009_alter_volunteerhour_time_in_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaverequest',
            name='status',
            field=models.IntegerField(choices=[(1, 'Active'), (2, 'Archived'), (3, 'Former'), (4, 'Delete'), (5, 'Pending'), (6, 'Accepted'), (7, 'Rejected'), (8, 'Approved')], default=5),
        ),
        migrations.AddField(
            model_name='leaverequest',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_by_leave_request', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='volunteerhour',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_by_volunteer_hour', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contractor',
            name='status',
            field=models.IntegerField(choices=[(1, 'Active'), (2, 'Archived'), (3, 'Former'), (4, 'Delete'), (5, 'Pending'), (6, 'Accepted'), (7, 'Rejected'), (8, 'Approved')], default=1),
        ),
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.IntegerField(choices=[(1, 'Active'), (2, 'Archived'), (3, 'Former'), (4, 'Delete'), (5, 'Pending'), (6, 'Accepted'), (7, 'Rejected'), (8, 'Approved')], default=1),
        ),
        migrations.AlterField(
            model_name='jobtitle',
            name='status',
            field=models.IntegerField(choices=[(1, 'Active'), (2, 'Archived'), (3, 'Former'), (4, 'Delete'), (5, 'Pending'), (6, 'Accepted'), (7, 'Rejected'), (8, 'Approved')], default=1),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='status',
            field=models.IntegerField(choices=[(1, 'Active'), (2, 'Archived'), (3, 'Former'), (4, 'Delete'), (5, 'Pending'), (6, 'Accepted'), (7, 'Rejected'), (8, 'Approved')], default=1),
        ),
        migrations.AlterField(
            model_name='volunteerhour',
            name='time_in',
            field=models.TimeField(default='08:28:06'),
        ),
        migrations.AlterField(
            model_name='volunteerhour',
            name='time_out',
            field=models.TimeField(default='08:28:06'),
        ),
        migrations.CreateModel(
            name='Policies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('policy_type', models.CharField(max_length=100)),
                ('url', models.URLField(blank=True, null=True)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (2, 'Archived'), (3, 'Former'), (4, 'Delete'), (5, 'Pending'), (6, 'Accepted'), (7, 'Rejected'), (8, 'Approved')], default=1)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_by_policy', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Policies',
            },
        ),
    ]
