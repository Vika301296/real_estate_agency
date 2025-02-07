from django.contrib import admin

from .models import Complaint, Flat, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flats.through
    extra = 5
    raw_id_fields = ('owner',)


@admin.register(Flat)
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


@admin.register(Complaint)
class СomplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
