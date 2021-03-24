from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import *
from pyPressApp.forms import *
import re
# Create your views here.


WEBPREFERENCES = Settings.objects.get(id=1)

DEFAULT_PAGE = WEBPREFERENCES.DefaultPage

def renderPages(request):
    
    slugGiven = request.get_full_path().replace('/', '')
    if slugGiven == "":
        slugGiven = DEFAULT_PAGE
    design = ThemeDesign.objects.get()
    pages = PyPress_Pages.objects.get(slug=cleanhtml(slugGiven))
    mThemeDesign =  design.HomePage
    userPost = RenderThemeVariables(mThemeDesign, pages)
    data = { "userPost": userPost }
    return render(request,"themeHolder.html",data)

def RenderThemeVariables(themeData,userPost):
    VarArray = ["$$USER_POST$$","$$USER_PAGE_NAME$$"]
    ValArray = [userPost.post,userPost.name]
    Variables = ThemeVariables.objects.all()
    for m_v in Variables:
        VarArray += m_v.VariableName
        ValArray += m_v.VariableData
    index = 0
    for var in VarArray:
        if themeData.find(var) != -1:
            themeData = themeData.replace(VarArray[index],ValArray[index])
        index = index + 1
    return themeData

# if Logged in .... 
def adminIndex(request):
    data = {"name":"name"}
    return render(request,"toDashboard.html",data)

def adminApps(request,appname):
    pages = PyPress_Pages.objects.all()
    counts= {"pageCount": pages.count(),}
    data = {"pageHeading": pageHeading(cleanhtml(appname)), "pageData":pages,"DBCounts":counts}
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
        myurl= "/pyadmin/pages/edit/"+ request.POST.get("slug")
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