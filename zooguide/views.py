from django.shortcuts import render

from .models import Animals, Exhibits, Tips, Schedule

def homepage(request):
    animals = Animals.objects.order_by('name')
    return render(request, 'zooguide/views.py')




def countydetail(request, county_slug):
    county = County.objects.get(name_slug=county_slug)
    lakes = Lake.objects.filter(county=county)
    return render(request, 'reports/countydetail.html', {'county': county, 'lakes':lakes})
