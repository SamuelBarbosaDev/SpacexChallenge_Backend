# Generated by Django 4.1.2 on 2022-10-11 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_alter_links_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='results',
            name='iid',
        ),
        migrations.AlterField(
            model_name='results',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
