# Generated by Django 3.0.4 on 2020-03-19 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20200319_2204'),
    ]

    operations = [
        migrations.RenameField(
            model_name='featuredproject',
            old_name='proj_id',
            new_name='proj',
        ),
    ]
