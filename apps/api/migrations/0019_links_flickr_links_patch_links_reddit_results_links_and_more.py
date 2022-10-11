# Generated by Django 4.1.2 on 2022-10-11 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_alter_results_fairings'),
    ]

    operations = [
        migrations.AddField(
            model_name='links',
            name='flickr',
            field=models.ManyToManyField(to='api.flickr'),
        ),
        migrations.AddField(
            model_name='links',
            name='patch',
            field=models.ManyToManyField(to='api.patch'),
        ),
        migrations.AddField(
            model_name='links',
            name='reddit',
            field=models.ManyToManyField(to='api.reddit'),
        ),
        migrations.AddField(
            model_name='results',
            name='links',
            field=models.ManyToManyField(to='api.links'),
        ),
        migrations.AlterField(
            model_name='flickr',
            name='original',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
