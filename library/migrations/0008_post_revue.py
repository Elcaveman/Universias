# Generated by Django 3.0.5 on 2020-05-31 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_auto_20200519_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='revue',
            field=models.CharField(blank=True, choices=[('SCOPUS', 'SCOPUS'), ('EBSCO', 'EBSCO'), ('DBLP', 'DBLP'), ('THOMSPON', 'THOMSPON')], max_length=10, null=True, verbose_name='Revue'),
        ),
    ]
