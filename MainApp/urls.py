from django.urls import path
from . import views

urlpatterns = [
    path('',views.Main,name='main'),
    path('directions/<str:type_>',views.streams,name='directs'),
    path('<str:type_>/<str:spec>_c_profilem_podgotovki_<str:programma>',views.ProgrammView,name='programm'),
    path('<str:type_>/<str:direct>',views.StreamView,name='one_direct'),
    path('instruction',views.Instruction,name='instruction'),
    path('proceed',views.HowToEnter,name='proceed'),
    path('question',views.SendQuestion,name='question')
    ]
