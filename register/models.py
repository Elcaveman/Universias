from django.db import models

from django.contrib.auth.models import User


#TODO: change the position to actual permissions/groups in auth.models

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

    POSITIONS=[('LC','Chef de Labo'),
    ('TL','Chef d\'équipe'),
    ('PM' , 'Membre Permanent'),
    ('AM' , 'Membre Associé')]
    #get_*field*_display
    DOMAINS = [('AI' ,'Artificial Intelligence'),('CL' ,' Computation and Language'),
    ('CC' ,'Computational Complexity'),('CE' ,'Computational Engineering, Finance, and Science'),
    ('CG' ,'Computational Geometry'),('GT' ,'Computer Science and Game Theory'),
    ('CV' ,'Computer Vision and Pattern Recognition'),('CY' ,'Computers and Society'),
    ('CR' ,'Cryptography and Security'),('DS' ,'Data Structures and Algorithms'),
    ('DB' ,'Databases'),('DL' ,'Digital Libraries'),('DM' ,'Discrete Mathematics'),
    ('Other',)*2
    ]
    profil_pic= models.ImageField("Profile", upload_to='users', height_field=None, width_field=None, max_length=None , blank=True)

    position = models.CharField(max_length=50, choices=POSITIONS,blank=True)
    domaine = models.CharField("Domaine of expertise", max_length=50,choices=DOMAINS)

    labo = models.ForeignKey("library.Laboratory" , on_delete=models.SET_NULL , null = True , blank=True)
    team = models.ForeignKey("library.Team" , on_delete=models.SET_NULL,null = True , blank=True)
  
    bio = models.TextField("Bio :", blank=True , help_text = "Say something about yourself")

    def __str__(self):
        return str(self.user.get_full_name())