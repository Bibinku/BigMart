from django.shortcuts import render,redirect
from BackEnd.models import CategoryDB,ProductDB
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from WebApp.models import ContactDB



# Create your views here.
def indexpage(req):
    return render(req,"index.html")
def addcategory(req):
    return render(req,"addcategory.html")

def savecategory(req):
    if req.method=="POST":
        a=req.POST.get('name')
        b=req.POST.get('description')
        img=req.FILES['image']
        obj=CategoryDB(name=a,description=b,image=img)
        obj.save()
        return redirect(indexpage)
def displaycategory(req):
    data=CategoryDB.objects.all()
    return render(req,"displaycategory.html" , {'data':data})

def editcategory(req,Cid):
    data=CategoryDB.objects.get(id=Cid)
    return render(req,"editcategory.html",{'data':data})

def updatecategory(req,Cid):
    if req.method=="POST":
        a=req.POST.get('name')
        b=req.POST.get('description')

        try:
           img=req.FILES['image']
           fs=FileSystemStorage()
           file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=CategoryDB.objects.get(id=Cid).image

    CategoryDB.objects.filter(id=Cid).update(name=a,description=b,image=file)
    return redirect(displaycategory)

def deletecategory(req,Cid):
    data=CategoryDB.objects.filter(id=Cid)
    data.delete()
    return redirect(displaycategory)

def adminlogin(req):
    return render(req,"adminlogin.html")

def admin(request):
    if request.method=="POST":
        a=request.POST.get('username')
        b=request.POST.get('pass')
        if User.objects.filter(username__contains=a).exists():
            x=authenticate(username=a,password=b)
            if x is not None:
                login(request,x)
                request.session['username']=a
                request.session['password']=b
                return redirect(indexpage)
            else:
                return redirect(adminlogin)
        else:
            return redirect(adminlogin)

def adminlogout(req):
    del req.session['username']
    del req.session['password']
    return redirect(adminlogin)

def addproduct(req):
    cat=CategoryDB.objects.all()
    return render(req,"product.html",{'cat':cat})

def saveproduct(req):
    if req.method=="POST":
        a=req.POST.get('category')
        b=req.POST.get('pname')
        c=req.POST.get('pprice')
        d=req.POST.get('pdescription')
        img=req.FILES['pimage']
        obj=ProductDB(category=a,pname=b,pprice=c,pdescription=d,pimage=img)
        obj.save()
        return redirect(indexpage)


def displayproduct(req):
    data=ProductDB.objects.all()
    return render(req,"displayproduct.html" , {'data':data})



def editproduct(req,Pid):
    data=ProductDB.objects.get(id=Pid)
    cat=CategoryDB.objects.all()
    return render(req,"Editproduct.html",{'data':data,'cat':cat})


def deleteproduct(req,Pid):
    data=ProductDB.objects.filter(id=Pid)
    data.delete()
    return redirect(displayproduct)

def updateproduct(req,Pid):
    if req.method=="POST":
        a = req.POST.get('category')
        b=req.POST.get('pname')
        c=req.POST.get('pprice')
        d=req.POST.get('pdescription')


        try:
           img=req.FILES['pimage']
           fs=FileSystemStorage()
           file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=ProductDB.objects.get(id=Pid).pimage

    ProductDB.objects.filter(id=Pid).update(category=a,pname=b,pprice=c,pdescription=d,pimage=file)
    return redirect(indexpage)

def displaycontact(req):
    data=ContactDB.objects.all()
    return render(req,"Displaycontact.html",{'data':data})

def deletecontact(req,CONid):
    data=ContactDB.objects.filter(id=CONid)
    data.delete()
    return redirect(displaycontact)