# Generated by Django 3.0.6 on 2020-06-27 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0021_auto_20200625_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='geo_lat',
            field=models.DecimalField(decimal_places=20, default=0, max_digits=23),
        ),
        migrations.AddField(
            model_name='listing',
            name='geo_lng',
            field=models.DecimalField(decimal_places=20, default=0, max_digits=23),
        ),
    ]
