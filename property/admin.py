from django.contrib import admin

from .models import Flat


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address']
    readonly_fields = ['construction_year']
    list_display = (
        'address', 'price', 'new_building', 'construction_year', 'town')
    list_display_links = None
    list_editable = ('address', 'price', 'new_building', 'construction_year')


admin.site.register(Flat, FlatAdmin)
