# Generated by Django 2.2.24 on 2023-10-26 11:31

from django.db import migrations


def set_new_builting(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat_construction_year = flat.construction_year
        if flat_construction_year >= 2015:
            flat.new_building = True
            flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(set_new_builting),
    ]