from django.shortcuts import render , redirect
from .models import *

# Create your views here.
def index(request):
    _users=User.objects.all()
    lastUser = User.objects.last()
    firstUser = User.objects.first()
    userswith24 = User.objects.filter().exclude()
    allUsers = User.objects.get(id=5)
    allUsers = User.objects.get(id=6)
    allUsers = User.objects.get(id=7)



    c = User.objects.get(id=6)
    c.lname = "Pancakes"
    c.save()



    context={
        'users':_users,
        'firstUser':firstUser,
        'lastUser' :lastUser,
        'userswith24':userswith24,
        'allUsers' :allUsers,

    }
    return render(request, 'index.html',context)

def create(request):
    if request.method=='POST':
        userhossam=User.objects.create(
            fname= request.POST['fname'],
            lname= request.POST['lname'],
            email= request.POST['email'],
            age= int(request.POST['age']),
        )
        userhossam.save()
    return redirect('/')

def destroy(request,user_id):
    x =User.objects.get(id=user_id)
    x.delete()

    return redirect('/')




    