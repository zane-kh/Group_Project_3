# Generated by Django 4.0.4 on 2022-05-02 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_service'),
        ('cal', '0003_event_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='service',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main_app.service'),
        ),
    ]
