# Generated by Django 3.1.1 on 2020-10-09 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_game'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='entry_num',
        ),
    ]