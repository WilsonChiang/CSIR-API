from django.db import models


class CountryReport(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "%s: %s" % (self.title, self.subtitle)


class Map(models.Model):
    country = models.CharField(max_length=255)  # TODO: Add choices enum for countries
    title = models.CharField(max_length=255)
    map_url = models.CharField(max_length=255)
    report = models.ForeignKey(CountryReport)
    
    def __str__(self):
        return '%s' % (self.title)


class Section(models.Model):
    title = models.CharField(max_length=255)
    report = models.ForeignKey(CountryReport)
    order = models.PositiveIntegerField()
    section = models.ForeignKey('self', related_name='section_section', blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return '%s' % self.title
