from django.urls import path
from WebApp import views

urlpatterns=[
    path('',views.homepage,name="homepage"),
    path('aboutpage/',views.aboutpage,name="aboutpage"),
    path('contactpage/',views.contactpage,name="contactpage"),
    path('ourproduct/',views.ourproduct,name="ourproduct"),
    path('savecontact/',views.savecontact,name="savecontact"),
    path('productfilter/<CatName>/',views.productfilter,name="productfilter"),
    path('singleproduct/<int:Pid>/',views.singleproduct,name="singleproduct"),
    path('registrarionpage/',views.registrarionpage,name="registrarionpage"),


]