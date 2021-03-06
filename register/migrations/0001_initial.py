# Generated by Django 3.0.5 on 2020-04-30 06:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('profil_pic', models.ImageField(blank=True, upload_to='users', verbose_name='Profile')),
                ('position', models.CharField(blank=True, choices=[('LC', 'Lab chief'), ('TL', 'Team leader'), ('PM', 'Permanent member'), ('AM', 'Associate member')], max_length=50)),
                ('domaine', models.CharField(max_length=50, verbose_name='Domaine of expertise')),
                ('bio', models.TextField(blank=True, help_text='Say something about yourself', verbose_name='Bio :')),
                ('labo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.Laboratory')),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.Team')),
            ],
        ),
    ]
