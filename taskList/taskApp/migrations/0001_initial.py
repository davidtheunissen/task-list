# Generated by Django 4.2.3 on 2024-01-17 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('status', models.CharField(choices=[('Todo', 'Todo'), ('Done', 'Done')], default='Todo', max_length=10)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
