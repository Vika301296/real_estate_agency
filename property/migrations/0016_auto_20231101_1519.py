# Generated by Django 2.2.24 on 2023-11-01 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_auto_20231101_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='text',
            field=models.TextField(verbose_name='Текст жалобы'),
        ),
    ]
