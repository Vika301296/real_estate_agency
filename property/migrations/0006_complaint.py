# Generated by Django 2.2.24 on 2023-10-26 21:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0005_auto_20231026_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=512, verbose_name='Текст жалобы:')),
                ('complainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaint', to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался:')),
                ('flat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaint', to='property.Flat', verbose_name='Квартира, на которую пожаловались:')),
            ],
        ),
    ]
