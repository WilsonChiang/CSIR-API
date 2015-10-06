from django.db import models


class CountryReport(models.Model):
    # This is a comment
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Maps(models.Model):
    country = models.CharField(max_length=255)  # TODO: Add choices enum for countries
    map_url = models.CharField(max_length=255)
    report = models.ForeignKey(CountryReport)


class Section(models.Model):
    title = models.CharField(max_length=255)
    report = models.ForeignKey(CountryReport)
    order = models.PositiveIntegerField()
    section = models.ForeignKey('self', related_name='section_section', blank=True, null=True)
    content = models.TextField(blank=True, null=True)
