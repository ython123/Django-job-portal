import imp
from django.contrib import admin

from . models import *
# Register your models here.


admin.site.register(Candidate)
admin.site.register(Company)
admin.site.register(UserMaster)
admin.site.register(Applyjob)
admin.site.register(Jobdetails)