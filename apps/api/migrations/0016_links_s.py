# Generated by Django 4.1.2 on 2022-10-11 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='links',
            name='s',
            field=models.ManyToManyField(to='api.fairings'),
        ),
    ]
