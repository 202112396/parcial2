# Generated by Django 5.0.2 on 2024-04-22 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_rename_user_usuarios'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='user_id',
        ),
    ]