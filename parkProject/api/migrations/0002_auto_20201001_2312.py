# Generated by Django 3.1.2 on 2020-10-02 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CarDetails',
            new_name='CarDetail',
        ),
        migrations.RenameModel(
            old_name='SlotDetails',
            new_name='SlotDetail',
        ),
    ]
