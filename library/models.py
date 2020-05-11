from django.db import models
from django.db import models
from django.contrib.postgres.fields import ArrayField

from register.models import Profile

class Team(models.Model):
    name = models.CharField("Team name", max_length=50)
    team_pic = models.ImageField(upload_to='teams', height_field=None, width_field=None,blank=True)
    labo = models.ForeignKey('library.Laboratory',on_delete=models.CASCADE,verbose_name="Laboratory")#!
    #? subjects = ArrayField(models.CharField(max_length=50))
    # this one might be usefull so instead of filtering by comparing the strings
    #  we can search trough a table of subjects to get a match wich is faster/memory friendly
    bio = models.TextField("Team Goal")

    def get_team_leader(self):
        set = Profile.objects.filter(position='TL',team=self.id)
        return set

    def get_perma_members(self):
        set = Profile.objects.filter(position='PM',team=self.id)
        return set
    def get_associate_members(self):
        set = Profile.objects.filter(position='AM',team=self.id)
        return set

    def __str__(self):
        return self.name
    

class Laboratory(models.Model):
    name = models.CharField("Lab name",max_length=80)
    labo_pic = models.ImageField(upload_to='labs', height_field=None, width_field=None,blank=True)
    bio = models.TextField("Lab Goal")

    def get_labo_chief(self):
        set = Profile.objects.filter(position='LC',team=self.id)
        return set
    def __str__(self):
        return self.name


class Post(models.Model):
    TYPES=[('Doc','Document'),('Prj' , 'Project') , ('CP','conference paper') , ('Brev','Brevet'),('Proto' , 'Prototype')]
    
    title = models.CharField(max_length=100)
    post_pic = models.ImageField(blank = True)
    pub_type = models.CharField("Post type", max_length=20,choices=TYPES)
    authors= models.ManyToManyField(to="register.Profile", related_name='owners')
    description = models.TextField()

    #extras/personal links
    URL = models.URLField(max_length=200)
    DOI = models.URLField(max_length=200)

    #Revues
    google_scholar = models.URLField("Google Scholar" ,max_length=200 ,help_text='click to search Google Scholar for this entry')
    bibtex = models.FileField('BIBTEX',upload_to='bibtex', max_length=100 , help_text='click to download the BibTEX formated file')

    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
