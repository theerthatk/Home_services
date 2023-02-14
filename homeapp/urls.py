from django.urls import path
from .views import *

urlpatterns=[
    path('index/',index),
    path('navbar/',navbar),
    path('register/',register),
    path('login/',login),
    path('empprofile/',empprofile),
    path('empupload/<int:id>',empupload),
    path('displayemp/',display_employees),
    path('editemp/<int:id>/', editemp),
    path('deleteemp/<int:id>/',deleteemp),
    path('userreg/', userreg),
    path('userlogin/',userlogin),
    path('userprofile/',userprofile),
    path('viewemp/',viewemp),
    path('userupload/<int:id>',userupload),
    path('displayuser/',displayuser),
    path('viewuser/',viewuser),
    path('edituser/<int:id>/', edituser),
    path('deleteuser/<int:id>/',deleteuser),
    path('applyemp/<int:id>/',applyemp),
    path('applyuser/<int:id>/',applyuser),
    # path('displayappliedemp/<int:id>/', displayappliedemp),
    path('viewappliedemployee/',viewappliedemployee),
    path('viewapplieduser/',viewapplieduser),
    path('userwishlist/<int:id>',userwishlist),
    path('userwishlistdisplay/',userwishlistdisplay),
    path('removeuserwishlist/<int:id>',removeuserwishlist),
    path('about/',about),
    path('services/',services),
    path('empwishlist/<int:id>', empwishlist),
    path('empwishlistdisplay/',empwishlistdisplay),
    path('removeempwishlist/<int:id>', removeempwishlist),





]