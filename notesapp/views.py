from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .models import Notes
# Create your views here.
def Signup(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['pas']
            if username and password:
                user = User.objects.create_user(username=username,password=password)
                if user:
                    return redirect("Login")
        return render(request,'signup.html')

def Login(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['pas']
            if username and password:
                user = authenticate(username=username,password=password)
                if user:
                    login(request,user)
                    return redirect("index")
        return render(request,'login.html')

def Index(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            title = request.POST['title']
            desc = request.POST['desc']
            done = Notes.objects.create(title=title,desc=desc,user=request.user)
        note = Notes.objects.filter(user=request.user)
        return render(request,'index.html',{'notes':note})
    else:
        return redirect("Login")

def Note(request,id):
    note = Notes.objects.get(id=id)
    return render(request,'note.html',{'note':note,'id':id})
    
def update(request,id):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        note = Notes.objects.filter(id=id).update(title=title,desc=desc)
        
    note =Notes.objects.get(id=id)
    
    return render(request,'update.html',{'note':note})

def delete(request,id):
    note = Notes.objects.filter(id=id).delete()
    if note:
        return redirect('/')
    return HttpResponse("TERA YEH NHI KARU GAAN ABHI DELETE")