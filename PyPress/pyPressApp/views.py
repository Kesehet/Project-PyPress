from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.






# if Logged in .... 
def adminIndex(request):
    data = {"name":"name"}
    return render(request,"adminIndex.html",data)

def adminApps(request,appname):
    data = {"name":"name"}
    if appname == "settings":
        return render(request,"adminSettings.html",data)
    if(appname == "home"):
        return render(request,"adminIndex.html",data)
    return render(request,"adminIndex.html",data)