#YOU NEED THESE TO IMPORT DATA

import os, sys, string, csv, datetime, time, django

# This line imports your settings. You need to change fooproject to the name of your project

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zoo.settings")

from django.conf import settings

#You need to change the next line to your app.models and import the name of the models in there.

from zooguide.models import Animals, Exhibits, Schedule

from django.template.defaultfilters import slugify, urlize

django.setup()

reader = csv.reader(open("animals.csv", "rU"), dialect=csv.excel)
reader.next()
for row in reader:
    exhibitname = row[0]
    animalname = row[1]

reader = csv.reader(open("exhibits.csv", "rU"), dialect=csv.excel)
reader.next()
for row in reader:
    #textexample = row[0]
    exhibitname = row[0]
    datefounded = row[1]
    cost = row[2]
    awardswon = row[3]
    lateattract = row[4]
    ilink = row[5]
    
reader = csv.reader(open("schedule.csv", "rU"), dialect=csv.excel)
reader.next()
    timeofday = row[0]
    event = row[1]
    location = row[2]

    #integerexample = int(row[1])
    #floatexample = float(row[2])
    #dateparseexample = time.strptime(row[3], "%m/%d/%Y %H:%M")
    #dateexample = datetime.datetime(dateparseexample.tm_year, dateparseexample.tm_mon, dateparseexample.tm_mday, dateparseexample.tm_hour, dateparseexample.tm_min)
    #modnam, modnamcreated = ModelName.objects.get_or_create(name=row[4], attribute=row[5])
    #anothermod, anothermodcreated = AnotherModel.objects.get_or_create(model=modnam, other_attribute=row[7])
    #print anothermod