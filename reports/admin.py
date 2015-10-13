from django.contrib import admin
from reports.models import CountryReport, Map, Section


class CountryReportAdmin(admin.ModelAdmin):
    model = CountryReport

class MapsAdmin(admin.ModelAdmin):
    model = Map

class SectionAdmin(admin.ModelAdmin):
    model = Section

admin.site.register(CountryReport)
admin.site.register(Map)
admin.site.register(Section)
