# Generated by Django 4.1.2 on 2022-10-09 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='spacex',
            options={'verbose_name_plural': 'Space X'},
        ),
        migrations.RenameField(
            model_name='spacex',
            old_name='name',
            new_name='message',
        ),
    ]
