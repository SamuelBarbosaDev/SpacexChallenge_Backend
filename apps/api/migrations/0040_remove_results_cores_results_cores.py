# Generated by Django 4.1.2 on 2022-10-13 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0039_alter_results_launch_library_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='results',
            name='cores',
        ),
        migrations.AddField(
            model_name='results',
            name='cores',
            field=models.ManyToManyField(to='api.cores'),
        ),
    ]