from django.shortcuts import render

from .models import Dest

def index(request):
    de= Dest.objects.all()
    return render(request,"index.html", {'de':de})

def post(request):

    if request.method == "POST":
        name=request.POST["name"]
        price=request.POST["price"]
        desc=request.POST["desc"]

        upload=Dest(name=name,price=price,desc=desc)
        upload.save()
        return render(request,'index.html')
    else:
        return render(request,'user.html')