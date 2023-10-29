from django.contrib import admin

from .models import Complaint, Flat, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.owned_flats.through
    extra = 5
    raw_id_fields = ('owner',)


class FlatAdmin(admin.ModelAdmin):
    list_filter = ('new_building',)
    search_fields = ['town', 'address']
    readonly_fields = ['construction_year']
    list_display = (
        'id', 'address', 'price', 'new_building',
        'construction_year', 'town', 'display_owners')
    list_display_links = None
    list_editable = ('address', 'price', 'new_building', 'construction_year')
    raw_id_fields = ('liked_by',)
    inlines = [OwnerInline]


class СomplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('owned_flats',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, СomplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
