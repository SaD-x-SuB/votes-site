# Generated by Django 4.1.5 on 2023-01-20 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_profile_createdreports_alter_profile_usedvotes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votes',
            name='date',
            field=models.DateField(blank=True, verbose_name='Дата'),
        ),
    ]
