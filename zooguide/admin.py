from django.contrib import admin

# Register your models here.
from .models import Animals

admin.site.register(Animals)

from .models import Exhibits

admin.site.register(Exhibits)