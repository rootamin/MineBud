# Generated by Django 4.1 on 2023-09-13 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='events',
            options={'ordering': ('-created',), 'verbose_name': 'Event', 'verbose_name_plural': 'Events'},
        ),
    ]
