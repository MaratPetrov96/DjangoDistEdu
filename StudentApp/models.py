from django.db import models
from MainApp.models import Region,Cathedra,Programm,Subject,Question
from django.core.validators import MaxValueValidator, MinValueValidator

class Profile(models.Model):
    USER_TYPES = (
        ('Преподаватель', 'Преподаватель'),
        ('Студент', 'Студент')
    )
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    user_type = models.CharField(max_length=13, choices=USER_TYPES)
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Teacher(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE,related_name='teacher')
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='teachers')
    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

class Group(models.Model):
    title = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

class Student(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE,related_name='student')
    group = models.ForeignKey(Group,on_delete=models.CASCADE,related_name='students')
    region = models.ForeignKey(Region,on_delete=models.CASCADE,related_name='students')
    cathedra = models.ForeignKey(Cathedra,on_delete=models.CASCADE,related_name='students')
    programm = models.ForeignKey(Programm,on_delete=models.CASCADE,related_name='students')
    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

class AcademicYear(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='students')
    number = models.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    class Meta:
        verbose_name = 'Курс студента'
        verbose_name_plural = 'Курсы студентов'

class Semester(models.Model):
    number = models.IntegerField(validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])
    year = models.ForeignKey(AcademicYear,on_delete=models.CASCADE,related_name='sems')
    is_session = models.BooleanField(default=False)
    session_time = models.CharField(max_length=8,choices=[('WI','Зимняя'),('SP','Весенняя'),('SU','Летняя'),('AU','Осенняя')])
    start = models.DateField()
    end = models.DateField()
    class Meta:
        verbose_name = 'Семестр'
        verbose_name_plural = 'Семестры'

class SemesterNow(models.Model):
    semester = models.OneToOneField(Semester,on_delete=models.CASCADE,related_name='now')
    student = models.OneToOneField(Student,on_delete=models.CASCADE,related_name='semester_now')

class SubjectInSem(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='sems')
    semester = models.ForeignKey(Semester,on_delete=models.CASCADE,related_name='subs')
    mark = models.BooleanField(blank=True,null=True)
    class Meta:
        verbose_name = 'Предмет в семестре'
        verbose_name_plural = 'Предменты семестра'

class Application(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='applications')
    context = models.TextField()
    date = models.DateField(auto_now_add=True)
    class Meta:
        verbose_name = 'Заявление'
        verbose_name_plural = 'Заявления'

class Exam(models.Model):
    subject = models.OneToOneField(SubjectInSem,on_delete=models.CASCADE,related_name='exam')
    mark = models.BooleanField(blank=True,null=True)
    class Meta:
        verbose_name = 'Экзамен'
        verbose_name_plural = 'Экзамены'

class Test(models.Model):
    subject = models.ForeignKey(SubjectInSem,on_delete=models.CASCADE,related_name='tests')
    mark = models.BooleanField(blank=True,null=True)
    class Meta:
        verbose_name = 'Контрольная'
        verbose_name_plural = 'Контрольные'

class TestQuestion(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='Tquests')
    test = models.ForeignKey(Test,on_delete=models.CASCADE,related_name='quests')
    student_answer = models.CharField(max_length=100,blank=True,null=True)
    mark = models.BooleanField(blank=True,null=True)
    class Meta:
        verbose_name = 'Вопрос контрольной'
        verbose_name_plural = 'Вопросы контрольных'

class ExamQuestion(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='Equests')
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE,related_name='quests')
    student_answer = models.CharField(max_length=100,blank=True,null=True)
    mark = models.BooleanField(blank=True,null=True)
    class Meta:
        verbose_name = 'Вопрос экзамена'
        verbose_name_plural = 'Вопросы экзаменов'

class StudentQuestion(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='questions')
    context = models.TextField()
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='questions',blank=True,null=True)
    date = models.DateField(auto_now_add=True)

class Letter(models.Model):
    from_user = models.ForeignKey(Profile,related_name='sent_letters',on_delete=models.CASCADE)
    to = models.ForeignKey(Profile,related_name='received_letters',on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    body = models.TextField(blank=True,null=True)
    date = models.DateField(auto_now_add=True)


class FileInLetter(models.Model):
    letter = models.ForeignKey(Letter,related_name='files',on_delete=models.CASCADE)
    file = models.FileField(upload_to='letters')
