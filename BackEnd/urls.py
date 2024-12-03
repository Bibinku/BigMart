from django.urls import path
from BackEnd import views

urlpatterns=[
    path('indexpage/',views.indexpage,name="indexpage"),
    path('addcategory/',views.addcategory,name="addcategory"),
    path('savecategory/',views.savecategory,name="savecategory"),
    path('displaycategory/',views.displaycategory,name="displaycategory"),
    path('editcategory/<int:Cid>/',views.editcategory,name="editcategory"),
    path('updatecategory/<int:Cid>/',views.updatecategory,name="updatecategory"),
    path('deletecategory/<int:Cid>/',views.deletecategory,name="deletecategory"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('admin/',views.admin,name="admin"),
    path('addproduct/',views.addproduct,name="addproduct"),
    path('adminlogout/',views.adminlogout,name="adminlogout"),
    path('saveproduct/',views.saveproduct,name="saveproduct"),
    path('displayproduct/',views.displayproduct,name="displayproduct"),
    path('editproduct/<int:Pid>/',views.editproduct,name="editproduct"),
    path('deleteproduct/<int:Pid>/',views.deleteproduct,name="deleteproduct"),
    path('updateproduct/<int:Pid>/',views.updateproduct,name="updateproduct"),
    path('displaycontact/',views.displaycontact,name="displaycontact"),
    path('deletecontact/<int:CONid>/',views.deletecontact,name="deletecontact"),





]