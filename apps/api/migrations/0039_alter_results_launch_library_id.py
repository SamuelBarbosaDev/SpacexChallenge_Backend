# Generated by Django 4.1.2 on 2022-10-13 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0038_results_auto_update_results_launch_library_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='launch_library_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
