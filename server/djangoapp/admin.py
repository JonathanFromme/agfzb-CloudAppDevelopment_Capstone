from django.contrib import admin
from .models import CarMake, CarModel


class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 2


class CarModelAdmin(admin.ModelAdmin):
    list_display = ['make', 'name', 'id', 'type', 'year']
    list_filter = ['type', 'make', 'id', 'year',]
    search_fields = ['name', 'type']


class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ('name', 'description')

# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)