# Generated by Django 4.1.2 on 2022-10-12 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_alter_fairings_ships'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fairings',
            name='ships',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]