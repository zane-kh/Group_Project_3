# Generated by Django 4.0.4 on 2022-05-04 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_remove_patient_services'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='services',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main_app.service'),
        ),
    ]
