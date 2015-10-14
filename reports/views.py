from rest_framework import viewsets
from reports.models import Maps, Section, CountryReport
from reports.serializers import MapsSerializer, SectionSerializer, CountryReportSerializer


class CountryReportViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = CountryReport.objects.all()
    serializer_class = CountryReportSerializer

class MapsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows maps to be viewed or edited.
    """
    queryset = Maps.objects.all()
    serializer_class = MapsSerializer


class SectionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows maps to be viewed or edited.
    """
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

# Create your views here.

#one that lists all country reports
#pass in the PK and the that PK's sections

