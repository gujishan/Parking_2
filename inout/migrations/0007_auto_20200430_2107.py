# Generated by Django 2.2 on 2020-04-30 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inout', '0006_auto_20200430_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parking',
            name='P_price',
            field=models.FloatField(blank=True, default=None, max_length=8, null=True),
        ),
    ]
