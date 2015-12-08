from django.contrib import admin

# Register your models here.
from .models import Animals, Exhibits, Schedule

admin.site.register(Animals)

admin.site.register(Exhibits)

admin.site.register(Schedule)