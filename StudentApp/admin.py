from django.contrib import admin
from .models import *

admin.site.register(Profile)
admin.site.register(Teacher)
admin.site.register(Group)
admin.site.register(Student)
admin.site.register(AcademicYear)
admin.site.register(Semester)
admin.site.register(SubjectInSem)
admin.site.register(Application)
admin.site.register(Exam)
admin.site.register(Test)
admin.site.register(TestQuestion)
admin.site.register(ExamQuestion)
