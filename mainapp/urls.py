
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home),
    path('fillform',views.fillform),
    path('createform',views.createform),
    path('savedetails',views.savedetails),
    path('fillform/<slug:formid>',views.fillform),
    path('saveresponse/<slug:formid>',views.saveresponse),
    path('getformbyid',views.getformbyid),
    path('fillformuser',views.fillformuser),
    path('showresponses/<slug:formid>/filter',views.showresponsepage),
    path('creatoraccesspage',views.creatorpageview),
]
