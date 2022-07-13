from django.http import HttpResponse
from django.shortcuts import render
from . import models
def index(request):
    u=models.User()
    if request.method == 'POST':
         #u.name=request.POST["user"]
         u.email=request.POST["email"]
         u.save()
         response=[x for x in models.User.objects.values() ]
         return HttpResponse(response)
    else:
        return render(request, 'home.html')
  
