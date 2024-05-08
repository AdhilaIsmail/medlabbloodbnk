# Generated by Django 4.2.4 on 2023-09-18 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.IntegerField(choices=[(1, 'DONOR'), (2, 'HOSPITAL'), (3, 'STAFF'), (4, 'REGISTEREDDONOR')], default='1'),
        ),
    ]
