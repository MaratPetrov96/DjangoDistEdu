# Generated by Django 4.0.4 on 2022-10-25 13:19

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
            ],
            options={
                'verbose_name': 'Курс студента',
                'verbose_name_plural': 'Курсы студентов',
            },
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Экзамен',
                'verbose_name_plural': 'Экзамены',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
            },
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('is_session', models.BooleanField(default=False)),
                ('session_time', models.CharField(choices=[('WI', 'Зимняя'), ('SP', 'Весенняя'), ('SU', 'Летняя'), ('AU', 'Осенняя')], max_length=8)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sems', to='StudentApp.academicyear')),
            ],
            options={
                'verbose_name': 'Семестр',
                'verbose_name_plural': 'Семестры',
            },
        ),
        migrations.CreateModel(
            name='SubjectInSem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.BooleanField(blank=True, null=True)),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subs', to='StudentApp.semester')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sems', to='MainApp.subject')),
            ],
            options={
                'verbose_name': 'Предмет в семестре',
                'verbose_name_plural': 'Предменты семестра',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.BooleanField(blank=True, null=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='StudentApp.subjectinsem')),
            ],
            options={
                'verbose_name': 'Контрольная',
                'verbose_name_plural': 'Контрольные',
            },
        ),
        migrations.CreateModel(
            name='TestQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_answer', models.CharField(blank=True, max_length=100, null=True)),
                ('mark', models.BooleanField(blank=True, null=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Tquests', to='MainApp.question')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quests', to='StudentApp.test')),
            ],
            options={
                'verbose_name': 'Вопрос контрольной',
                'verbose_name_plural': 'Вопросы контрольных',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cathedra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='MainApp.cathedra')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='StudentApp.group')),
                ('programm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='MainApp.programm')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='MainApp.region')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='MainApp.user')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
            },
        ),
        migrations.CreateModel(
            name='ExamQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_answer', models.CharField(blank=True, max_length=100, null=True)),
                ('mark', models.BooleanField(blank=True, null=True)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quests', to='StudentApp.exam')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Equests', to='MainApp.question')),
            ],
            options={
                'verbose_name': 'Вопрос экзамена',
                'verbose_name_plural': 'Вопросы экзаменов',
            },
        ),
        migrations.AddField(
            model_name='exam',
            name='subject',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='exam', to='StudentApp.subjectinsem'),
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='StudentApp.student')),
            ],
            options={
                'verbose_name': 'Заявление',
                'verbose_name_plural': 'Заявления',
            },
        ),
        migrations.AddField(
            model_name='academicyear',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='StudentApp.student'),
        ),
    ]