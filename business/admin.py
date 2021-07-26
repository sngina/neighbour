from django.contrib import admin
from.models import Neighbourhood ,Business ,Profile
# Register your models here.

class NeighbourhoodAdmin(admin.ModelAdmin):
    list_display = ('name' , 'location' , 'occupants')

class BusinessAdmin(admin.ModelAdmin):
    filter_horizontal = ('image' ,)

admin.site.register(Neighbourhood)
admin.site.register(Profile)
admin.site.register(Business)