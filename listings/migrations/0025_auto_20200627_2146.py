# Generated by Django 3.0.6 on 2020-06-27 21:46

from django.db import migrations
import listings.forms


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0024_auto_20200627_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='hidden',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='lot_size',
        ),
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=listings.forms.NonStrippingTextField(blank=True),
        ),
    ]
