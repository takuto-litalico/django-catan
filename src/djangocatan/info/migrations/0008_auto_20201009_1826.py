# Generated by Django 3.1.1 on 2020-10-09 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0007_auto_20201009_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='game',
        ),
        migrations.RemoveField(
            model_name='score',
            name='player',
        ),
        migrations.AddField(
            model_name='score',
            name='player',
            field=models.ManyToManyField(related_name='scores', to='info.Player'),
        ),
    ]
