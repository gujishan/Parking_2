# Generated by Django 2.2 on 2020-04-30 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inout', '0004_delete_pritest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parking',
            name='P_price',
            field=models.FloatField(blank=True, default=None, max_length=8, null=True),
        ),
    ]