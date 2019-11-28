# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2019-02-12 06:08


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ctim', '0005_auto_20190208_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aliases',
            name='user',
        ),
        migrations.RemoveField(
            model_name='config',
            name='default_taxii',
        ),
        migrations.RemoveField(
            model_name='ctirsconfig',
            name='user',
        ),
        migrations.DeleteModel(
            name='Aliases',
        ),
        migrations.DeleteModel(
            name='Config',
        ),
        migrations.DeleteModel(
            name='CtirsConfig',
        ),
        migrations.DeleteModel(
            name='Taxii',
        ),
    ]
