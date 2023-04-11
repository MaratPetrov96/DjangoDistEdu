from django.urls import path
from . import views

urlpatterns = [
    path('',views.student_main,name='main'),
    path('application',views.ApplicationFromStudent,name='application'),
    path('question',views.QuestionFromStudent,name='question'),
    path('from_student',views.SendWork,name='from_student')
    ]
