# Generated by Django 5.0.6 on 2024-06-21 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='slug',
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
