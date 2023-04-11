from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

@login_required
def student_main(request):
    if request.user.user_type == 'Студент':
        return render(request,'Main.html',{'student':request.user})

@login_required
def ApplicationFromStudent(request):
    if request.method == 'POST':
        Application(student=request.user.student)
    return render(request,'Application.html')

@login_required
def TestPage(request):
    if request.user.user_type == 'Студент':
        return render(request,'Test.html')

@login_required
def QuestionFromStudent(request):
    if request.user.user_type == 'Студент':
        if request.method == 'POST':
            new = Letter(from_user=request.user,to=request.method['test'],
                         context=request['context'],
                         body=request.POST['body'])
            if request['theme'] != 'noTheme':
                new.subject = request['theme']
            new.save()
        return render(request,'QuestionForm.html')

@login_required
def SendWork(request,subject_in_sem):
    new = Letter(from_user=request.user,to=Profile.objects.get(pk=2),
                 subject=subject_in_sem.subject.title)

@login_required
def LetterForm(request):
    return render(request,'LetterForm.html')

@login_required
def sendLetter(request,u_id):
    new = Letter(from_user=request.user,to=User.objects.get(pk=u_id)
           ,subject=request.POST['subject'],body=request.POST['body'])
    new.save()
    return render(request,'LetterSuccess.html')
