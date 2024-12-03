from django.shortcuts import render,redirect
from BackEnd.models import ProductDB,CategoryDB
from WebApp.models import ContactDB


# Create your views here.

def homepage(req):
    data=CategoryDB.objects.all()
    return render(req,"home.html", {'data':data})

def aboutpage(req):
    data=CategoryDB.objects.all()
    return render(req,"about.html", {'data':data})


def contactpage(req):
    data=CategoryDB.objects.all()
    return render(req,"contact.html", {'data':data})


def ourproduct(req):
    pro=ProductDB.objects.all()
    data=CategoryDB.objects.all()

    return render(req,"Ourproduct.html",{'pro':pro,'data':data})

def savecontact(req):
    if req.method=="POST":
        a=req.POST.get('name')
        b=req.POST.get('email')
        c=req.POST.get('phone')
        d=req.POST.get('subject')
        f=req.POST.get('message')
        obj=ContactDB(name=a,email=b,phone=c,subject=d,message=f)
        obj.save()
        return redirect(contactpage)

def productfilter(req,CatName):

    data=ProductDB.objects.filter(category=CatName)
    return render(req,"productsfiltered.html",{'data': data})

def singleproduct(req,Pid):
    data=ProductDB.objects.get(id=Pid)
    return render(req,"singleproduct.html",{'data':data})

def registrarionpage(req):
    return render(req,"registration.html")