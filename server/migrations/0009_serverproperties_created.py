# Generated by Django 4.2.5 on 2023-09-24 11:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0008_alter_serverproperties_allow_nether_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='serverproperties',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
