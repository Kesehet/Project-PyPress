from django.shortcuts import render
from django.http import HttpResponse
import re
# Create your views here.






# if Logged in .... 
def adminIndex(request):
    data = {"name":"name"}
    return render(request,"toDashboard.html",data)

def adminApps(request,appname):
    data = {"pageHeading": pageHeading(cleanhtml(appname))}
    if appname == "settings":
        return render(request,"adminSettings.html",data)
    if(appname == "home"):
        return render(request,"adminIndex.html",data)
    if(appname == "pages"):
        return render(request,"adminPages.html",data)
    if(appname == "posts"):
        return render(request,"adminPosts.html",data)
    return render(request,"adminIndex.html")


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