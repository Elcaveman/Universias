# Generated by Django 3.0.5 on 2020-05-31 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20200512_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(blank=True, choices=[('LC', 'Chef de Labo'), ('TL', "Chef d'équipe"), ('PM', 'Membre Permanent'), ('AM', 'Membre Associé')], max_length=50),
        ),
    ]