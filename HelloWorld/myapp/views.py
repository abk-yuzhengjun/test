from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import User


# Create your views here.
def register(request):
    status = 'Success!'
    username = ''
    password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        try:
            q = User(username=username,password=password)
            q.save()
        except:
            status = 'register error!'
        else:
            status = 'Success!'
    else:
        status = ''
    return render(request, 'myapp/register.html', {'status': status,'username':username,'password':password})


def login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        result = User.objects.filter(username=username)
        try:
            for user in result:
                if user.password == password:
                    return HttpResponse("Welcome %s " % username)
        except:
            return Http404()
        return HttpResponse("It is not a user, %s" % username)
    return render(request,'myapp/login.html')
