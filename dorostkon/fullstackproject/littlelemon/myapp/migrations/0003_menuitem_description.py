# Generated by Django 4.2.5 on 2023-12-09 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_menuitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='description',
            field=models.CharField(default='none', max_length=200),
        ),
    ]
