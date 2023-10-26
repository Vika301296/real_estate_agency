from django.contrib import admin

from .models import Complaint, Flat


class FlatAdmin(admin.ModelAdmin):
    list_filter = ('new_building',)
    search_fields = ['town', 'address']
    readonly_fields = ['construction_year']
    list_display = (
        'address', 'price', 'new_building', 'construction_year', 'town')
    list_display_links = None
    list_editable = ('address', 'price', 'new_building', 'construction_year')


class СomplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, СomplaintAdmin)
