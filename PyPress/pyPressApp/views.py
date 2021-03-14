from django.shortcuts import render
from django.http import HttpResponse
from .models import PyPress_Pages
import re
# Create your views here.






# if Logged in .... 
def adminIndex(request):
    data = {"name":"name"}
    return render(request,"toDashboard.html",data)

def adminApps(request,appname):
    pages = PyPress_Pages.objects.all()
    data = {"pageHeading": pageHeading(cleanhtml(appname)), "pageData":pages}
    if appname == "settings":
        return render(request,"adminSettings.html",data)
    if(appname == "home"):
        return render(request,"adminIndex.html",data)
    if(appname == "pages"):
        return render(request,"adminPages.html",data)
    if(appname == "posts"):
        return render(request,"adminPosts.html",data)
    return render(request,"adminIndex.html")

def adminEditPage(request,editPageSlug):
    data = {"pageHeading": cleanhtml(editPageSlug)}
    return render(request,'adminEditPage.html',data)


def cleanhtml(raw_html):
  cleanr =  re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

def pageHeading(name):
    if name == "home":
        return "Dashboard"
    if name == "settings":
        return "Settings"
    if name == "posts":
        return "Posts"
    if name == "pages":
        return "Pages"