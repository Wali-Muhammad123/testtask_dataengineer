# Generated by Django 5.0.2 on 2024-02-16 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_poi_internal_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poi',
            name='category',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
