from django.shortcuts import render

# Create your views here.
from zooguide.models import Animals, Exhibits, Schedule

def homepage(request):
    exhibits = Exhibits.objects.order_by('exhibit_name')
    context = {"exhibits":exhibits}
    return render(request, 'index.html', context)

def exhibitdetail(request, exhibit_number):
    exhibit = Exhibits.objects.get(id=exhibit_number)
    context = {"exhibit":exhibit}
    return render(request, 'exhibitdetail.html', context)

def exhibitlist(request):
    exhibits = Exhibits.objects.order_by('exhibit_name')
    context = {"exhibits":exhibits}
    return render(request, 'exhibits.html', context)

def schedule(request):
    context = {"schedule":schedule}
    return render(request, 'schedule.html', context)

