# Generated by Django 4.0.4 on 2022-10-26 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StudentApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SemesterNow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='now', to='StudentApp.semester')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='semester_now', to='StudentApp.student')),
            ],
        ),
    ]
