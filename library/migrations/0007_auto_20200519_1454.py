# Generated by Django 3.0.5 on 2020-05-19 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20200519_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='team_pic',
            field=models.ImageField(blank=True, upload_to='teams'),
        ),
    ]
