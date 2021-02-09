from django.contrib import admin
from .models import Schools, Scrapy_Switch
from django.contrib import messages


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('sch_nm', 'region', 'updated')
    list_filter = (
        'region',
    )
    search_fields = ('sch_nm',)


class scrapy_admin(admin.ModelAdmin):
    list_display = ('switch', 'active','last_on')

    def active(self, obj):
        return obj.switch == 1

    active.boolean = True

    def make_active(modeladmin, request, queryset):
        queryset.update(switch=1)
        messages.success(
            request, "Selected Record(s) Marked as Active Successfully !!")

    def make_inactive(modeladmin, request, queryset):
        queryset.update(switch=0)
        messages.success(
            request, "Selected Record(s) Marked as Inactive Successfully !!")

    admin.site.add_action(make_active, "Make Active")
    admin.site.add_action(make_inactive, "Make Inactive")


admin.site.register(Schools, SchoolAdmin)
admin.site.register(Scrapy_Switch, scrapy_admin)
