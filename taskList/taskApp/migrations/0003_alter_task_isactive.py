# Generated by Django 4.2.3 on 2024-01-17 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskApp', '0002_remove_task_status_task_isactive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
    ]