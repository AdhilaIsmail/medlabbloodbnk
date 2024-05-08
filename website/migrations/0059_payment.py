# Generated by Django 4.2.4 on 2023-10-19 10:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0058_rename_donteddonor_donateddonor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_amount', models.DecimalField(decimal_places=2, default=1, max_digits=10)),
                ('payment_status', models.CharField(choices=[('Pending', 'Pending'), ('Success', 'Success')], default='Pending', max_length=10)),
                ('payment_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
