# Generated by Django 4.0.4 on 2023-01-26 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentApp', '0010_letter_fileinletter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
