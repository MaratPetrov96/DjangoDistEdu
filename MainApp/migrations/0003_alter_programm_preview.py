# Generated by Django 4.0.4 on 2022-10-25 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_programm_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programm',
            name='preview',
            field=models.ImageField(upload_to='upload'),
        ),
    ]