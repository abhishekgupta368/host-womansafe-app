from django.contrib import admin
from .models import Police
from .models import Location

# Register your models here.
admin.site.register(Police)
admin.site.register(Location)