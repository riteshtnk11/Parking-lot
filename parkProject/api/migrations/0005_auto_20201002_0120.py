# Generated by Django 3.1.2 on 2020-10-02 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20201002_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slotdetail',
            name='carNumber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cardetail'),
        ),
    ]
