# Generated by Django 4.0.4 on 2022-10-25 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_alter_programm_preview'),
    ]

    operations = [
        migrations.AddField(
            model_name='speciality',
            name='preview',
            field=models.ImageField(blank=True, upload_to='upload'),
        ),
    ]
