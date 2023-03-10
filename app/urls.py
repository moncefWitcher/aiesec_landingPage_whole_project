from django.urls import path 
from . import views 


urlpatterns = [
     path('', views.Home ) ,
     path('about/', views.About ) ,
     path('events/', views.events ) ,
     path('contact/', views.Contact ) ,
     path('log/singin/', views.SigIn ) ,
     path('log/in/', views.Login ) ,
     path('log/changepassword/', views.ChangePassword ) ,
     path('mc_info/create/', views.createMC ) ,
     path('mc_info/team_members/create/', views.createMCteamMembers ) ,
     path('lc_info/create/', views.createLCembers ) ,
     path('lc_info/members/create/', views.createLCteamMembers ) ,
     path('event/insert/', views.AddEvent ) ,
     path('question_answer/insert/', views.AddFQ ) ,
     path('form/insert/', views.AddForms ) ,
]