# Generated by Django 4.1 on 2023-09-15 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='profile_pic',
            field=models.ImageField(default='steve.png', upload_to='profiles/'),
        ),
    ]
