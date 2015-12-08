from django.shortcuts import render

# Create your views here.
from zooguide.models import Animals, Exhibits

def homepage(request):
    exhibits = Exhibits.objects.order_by('exhibit_name')
    return render(request, 'index.html', context)


#def countydetail(request, county_slug):
#    county = County.objects.get(name_slug=county_slug)
#    lakes = Lake.objects.filter(county=county)
#    return render(request, 'reports/countydetail.html', {'county': #county, 'lakes':lakes})
