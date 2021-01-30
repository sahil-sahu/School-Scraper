from django.contrib import admin 
from .models import Schools 
  
class SchoolAdmin(admin.ModelAdmin): 
    list_display = ('sch_nm', 'updated') 
  
admin.site.register(Schools, SchoolAdmin) 
