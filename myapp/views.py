from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegister
from .models import User
# Create your views here.


def add_view(request):
    if request.method == "POST":
        fm = StudentRegister(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm,email=em,password=pw)
            reg.save()
            fm = StudentRegister()

    else:
        fm = StudentRegister()
    stud = User.objects.all()


    return render(request,'main.html',{'form':fm,'stud':stud})



#delete data 

def delete_data(request,id):
    if request.method=="POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')



def update_view(request,id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        fm = StudentRegister(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegister(instance=pi)

    return render(request,'update.html',{'form':fm})
