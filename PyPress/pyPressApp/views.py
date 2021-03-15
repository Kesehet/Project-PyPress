from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import *
from pyPressApp.forms import *
import re
# Create your views here.



def renderPages(request):
    pages = PyPress_Pages.objects.get(slug=cleanhtml(request.get_full_path().replace('/', '')))
    userPost = pages.post
    data = { "userPost": userPost }
    return render(request,"themeHolder.html",data)

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
    try:
        page = PyPress_Pages.objects.get(slug=cleanhtml(editPageSlug))
    except:
        return render(request,'404.html')
    if request.method == "POST":
        myurl= "/pyadmin/edit/"+ request.POST.get("slug")
        page.name=request.POST.get("name")
        page.slug=request.POST.get("slug")
        page.post=request.POST.get("post")
        page.save()
        data = {"pageHeading": cleanhtml(editPageSlug), "pageData": page}
        return redirect (myurl)
    else:
        data = {"pageHeading": cleanhtml(editPageSlug), "pageData": page }
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