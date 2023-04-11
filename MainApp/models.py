from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Region(models.Model):
    title = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'

class Subject(models.Model):
    title = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

class Cathedra(models.Model):
    title = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10)
    class Meta:
        verbose_name = 'Кафедра'
        verbose_name_plural = 'Кафедры'

class Stream(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    code = models.CharField(max_length=2)
    preview = models.ImageField(upload_to='upload',blank=True)
    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'
    def __str__(self):
        return self.title

class Speciality(models.Model):
    BC = 'Bach'
    MG = 'Mag'
    stream = models.ForeignKey(Stream,on_delete=models.CASCADE,related_name='specials')
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    degree = models.CharField(max_length=10,choices=([(BC,'Бакалавриат'),(MG,'Магистратура')]))
    code = models.CharField(max_length=2)
    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'
    def __str__(self):
        return self.title

class Programm(models.Model):
    special = models.ForeignKey(Speciality,on_delete=models.CASCADE,related_name='progs')
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    preview = models.ImageField(upload_to='upload',blank=True)
    description = models.TextField(blank=True,null=True)
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
    def __str__(self):
        return self.title

"""class User(AbstractBaseUser):
    USER_TYPES = (
        ('Преподаватель', 'Преподаватель'),
        ('Студент', 'Студент')
    )
    login = models.CharField(max_length=100,blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    user_type = models.CharField(max_length=13, choices=USER_TYPES)
    USERNAME_FIELD = 'login'
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'"""

class Material(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='materials')
    file = models.FileField(upload_to='materials')
    class Meta:
        verbose_name = 'Учебный материал'
        verbose_name_plural = 'Учебные материалы'

class Question(models.Model):
    content = models.TextField()
    answer = models.TextField()
    options = models.TextField()
    kind = models.CharField(max_length=10,choices=(
        [('one','Ввод ответа'),
         ('radio','Один из нескольких'),
         ('select','Выпадающие списки'),
         ('check','Не менее одного ответа')
         ]))
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class Review(models.Model):
    student_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='reviews',blank=True,null=True)
    special = models.ForeignKey(Speciality,on_delete=models.CASCADE,related_name='reviews')
    content = models.TextField()
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

'''class SubjectInDescription(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='in_descrs')
    programm = models.ForeignKey(Programm,on_delete=models.CASCADE,related_name='subjects')
    semester = models.IntegerField()'''
