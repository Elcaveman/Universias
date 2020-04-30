# Generated by Django 3.0.5 on 2020-04-30 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Lab name')),
                ('labo_pic', models.ImageField(blank=True, upload_to='labs')),
                ('bio', models.TextField(verbose_name='Lab Goal')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('post_pic', models.ImageField(blank=True, upload_to='')),
                ('pub_type', models.CharField(choices=[('Doc', 'Document'), ('Prj', 'Project'), ('CP', 'conference paper'), ('Brev', 'Brevet'), ('Proto', 'Prototype')], max_length=20, verbose_name='Post type')),
                ('description', models.TextField()),
                ('URL', models.URLField()),
                ('DOI', models.URLField()),
                ('google_scholar', models.URLField(help_text='click to search Google Scholar for this entry', verbose_name='Google Scholar')),
                ('bibtex', models.FileField(help_text='click to download the BibTEX formated file', upload_to='bibtex', verbose_name='BIBTEX')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Team name')),
                ('team_pic', models.ImageField(blank=True, upload_to='teams')),
                ('bio', models.TextField(verbose_name='Team Goal')),
                ('labo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Laboratory', verbose_name='Laboratory')),
            ],
        ),
    ]
