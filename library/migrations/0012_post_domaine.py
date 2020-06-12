# Generated by Django 3.0.5 on 2020-06-11 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0011_auto_20200601_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='domaine',
            field=models.CharField(blank=True, choices=[('LC', 'Chef de Labo'), ('TL', "Chef d'équipe"), ('PM', 'Membre Permanent'), ('AM', 'Membre Associé')], max_length=100, null=True, verbose_name='Domaine'),
        ),
    ]