from django.shortcuts import render,redirect,reverse,HttpResponse
from .models import *
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout
#from StudentApp import

#special_degrees = {'Bach':'Б','Mag':''}

def header(request,template,args):
    args
    return render(request,template,args)

def Main(request):
    #print(Speciality.objects.all())
    return render(request,'Main.html',{'specialities':Speciality.objects.all()})

def streams(request,type_):
    specs = Speciality.objects.filter(degree=type_.capitalize())
    return render(request,'Streams.html',{'type':type_.capitalize(),'specialities':specs,'range':range(1,10)})

def HowToEnter(request):
    return render(request,'HowToEnter.html')

def Instruction(request):
    return render(request,'Instruction.html')

def ProgrammView(request,type_,spec,programma):
    return render(request,'ProgrammPage.html',{'programm':Programm.objects.get(url=programma),'range':range(1,10)})
    #return HttpResponse(Programm.objects.get(url=programma).title)

def Login(request):
    #return redirect(reverse('login'))
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username, password=password)
        if user:
            login(request,user)
            return redirect('StudentApp.main')
    return render(request,'Login.html')

def Application(request,profile):
    if request.method == 'POST':
        pass
    return render(request,'ApplicationPage.html')

def StreamView(request,type_,direct):
    direct = Stream.objects.get(url=direct)
    return render(request,'DirectPage.html',{'type':type_,'direct':direct,'all_specs':Speciality.objects.filter(degree=type_.capitalize())
                                             ,'specs':direct.specials.filter(degree=type_.capitalize())
                                              ,'range':range(1,10)})

def SendQuestion(request):
    send_mail(
    'Вопрос от абитуриента',
    f"""{request.POST['uname']} из города {request.POST['city']}\r\n\r\n
    {request.POST['context']}\r\n\r\n
    {request.POST['email']}""",
    'maratpython@yandex.ru',
    ['maratpython@yandex.ru']
    ,fail_silently=False
    )
    return redirect('main')

def StartStudy(request,pk):
    profile = Programm.objects.get(pk=pk)
    send_mail(
    'Заявка на обучение от абитуриента',
    f"""{request.POST['uname']} из города {request.POST['city']},
    {request.POST['country']} желает поступить на специальность
    '{profile.special}' по профилю '{profile}'\r\n\r\n
    {request.POST['email']}""",
    'maratpython@yandex.ru',
    ['maratpython@yandex.ru']
    ,fail_silently=False
    )
    return redirect('main')
