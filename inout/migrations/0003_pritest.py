# Generated by Django 2.2 on 2020-04-30 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inout', '0002_parking'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_pic', models.ImageField(upload_to='')),
            ],
        ),
    ]
