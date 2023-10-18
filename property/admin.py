from django.contrib import admin

from .models import Flat


# admin.site.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address']


admin.site.register(Flat, FlatAdmin)
