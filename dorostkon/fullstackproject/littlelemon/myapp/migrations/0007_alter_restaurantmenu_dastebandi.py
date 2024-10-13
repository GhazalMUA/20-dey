# Generated by Django 5.0 on 2023-12-14 11:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_dastebandi_restaurantmenu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantmenu',
            name='dastebandi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.dastebandi'),
        ),
    ]
