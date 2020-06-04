# Generated by Django 3.0.5 on 2020-05-31 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_auto_20200531_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='revue',
            field=models.CharField(blank=True, choices=[('SCOPUS', 'SCOPUS'), ('EBSCO', 'EBSCO'), ('DBLP', 'DBLP'), ('THOMPSON', 'THOMPSON')], max_length=10, null=True, verbose_name='Revue'),
        ),
    ]
