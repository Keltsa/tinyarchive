# Generated by Django 4.0.5 on 2023-08-08 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0015_rename_location_artifact_purchase_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='artifact',
            name='sentimental_value',
            field=models.TextField(blank='True', max_length=500),
        ),
    ]
