# Generated by Django 5.0.2 on 2024-04-22 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0005_usuarios_age_usuarios_dpi_usuarios_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='tel',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
