# Generated by Django 2.2 on 2020-04-27 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('Car_no', models.CharField(max_length=32, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
