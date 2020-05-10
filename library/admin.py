from django.contrib import admin
from . import models as m
# Register your models here.
admin.site.register(m.Post)
admin.site.register(m.Laboratory)
admin.site.register(m.Team)
admin.site.register(m.Profile)