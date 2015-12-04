#YOU NEED THESE TO IMPORT DATA
​
import os, sys, string, csv, datetime, time, django
​
# This line imports your settings. You need to change fooproject to the name of your project
​
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fooproject.settings")
​
from django.conf import settings
​
#You need to change the next line to your app.models and import the name of the models in there.
​
from appname.models import ModelName, AnotherModel, ThirdModel
​
from django.template.defaultfilters import slugify, urlize
​
django.setup()
​
reader = csv.reader(open("salaries1314.csv", "rU"), dialect=csv.excel)
reader.next()
for row in reader:
    textexample = row[0]
    integerexample = int(row[1])