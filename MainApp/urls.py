from django.urls import path,include
from . import views
from StudentApp import views as student_views

urlpatterns = [
    path('login',views.Login,name='login'),
    path('',views.Main,name='main'),
    path('start/<int:pk>',views.StartStudy,name='start_study'),
    path('directions/<str:type_>',views.streams,name='directs'),
    path('<str:type_>/<str:spec>_c_profilem_podgotovki_<str:programma>',views.ProgrammView,name='programm'),
    path('<str:type_>/<str:direct>',views.StreamView,name='one_direct'),
    path('instruction',views.Instruction,name='instruction'),
    path('proceed',views.HowToEnter,name='proceed'),
    path('question',views.SendQuestion,name='question'),
    path('lk',student_views.student_main)
    ]
