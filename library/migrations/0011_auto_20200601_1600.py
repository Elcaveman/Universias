# Generated by Django 3.0.5 on 2020-06-01 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0010_auto_20200531_1750'),
    ]

    operations = [
        migrations.CreateModel(
            name='Revue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Revue Name')),
                ('image', models.ImageField(upload_to='revues', verbose_name='Revue Image')),
                ('URL', models.URLField(verbose_name='URL')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='revue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.Revue'),
        ),
    ]
