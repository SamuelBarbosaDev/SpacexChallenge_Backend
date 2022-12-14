# Generated by Django 4.1.2 on 2022-10-11 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_fairings_ships_alter_flickr_small_ships_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fairings',
            name='ships',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='flickr',
            name='small_ships',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='results',
            name='capsules_ships',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='results',
            name='crew_ships',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='results',
            name='failures_ships',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='results',
            name='payloads_ships',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='results',
            name='ships_ships',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
