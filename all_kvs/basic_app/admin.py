from django.contrib import admin 
from .models import Schools 

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('sch_nm','region', 'updated') 
    list_filter = (
        'region',
    )
    search_fields = ('sch_nm',)


admin.site.register(Schools, SchoolAdmin) 
