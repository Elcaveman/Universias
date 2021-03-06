# Generated by Django 3.0.5 on 2020-06-12 00:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0012_post_domaine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='domaine',
            field=models.CharField(blank=True, choices=[('AI', 'Artificial Intelligence'), ('CL', ' Computation and Language'), ('CC', 'Computational Complexity'), ('CE', 'Computational Engineering, Finance, and Science'), ('CG', 'Computational Geometry'), ('GT', 'Computer Science and Game Theory'), ('CV', 'Computer Vision and Pattern Recognition'), ('CY', 'Computers and Society'), ('CR', 'Cryptography and Security'), ('DS', 'Data Structures and Algorithms'), ('DB', 'Databases'), ('DL', 'Digital Libraries'), ('DM', 'Discrete Mathematics'), ('Other', 'Other')], max_length=100, null=True, verbose_name='Domaine'),
        ),
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
