# Generated by Django 4.1.2 on 2022-10-12 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_alter_fairings_ships'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fairings',
            name='ships',
            field=models.JSONField(default=list),
        ),
    ]