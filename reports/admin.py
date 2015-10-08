from django.contrib import admin
from reports.models import CountryReport
from reports.models import Maps
from reports.models import Section

class CountryReportAdmin(admin.ModelAdmin):
    model = CountryReport
    
class MapsAdmin(admin.ModelAdmin):
    model = Maps

class SectionAdmin(admin.ModelAdmin):
    model = Section

admin.site.register(CountryReport)
admin.site.register(Maps)
admin.site.register(Section)