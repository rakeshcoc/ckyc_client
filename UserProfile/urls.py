from django.contrib import admin
from django.urls import path
from . import views 
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
# from django.contrib.auth import views as auth_views
app_name ='UserProfile'
urlpatterns = [
   path('register/',views.register,name='register'),
   path('logout/',LogoutView.as_view(),name='logout'),
   path('login/', LoginView.as_view(redirect_authenticated_user=True),name='login'),
   path('reset-password/', views.change_password, name='change_password'),
   path('myprofile/<str:username>/', views.user_detail,name='userdetail'),
   path('myprofile/<str:username>/edit', views.user_update,name='update'),

   path('myprofile-settings/',views.user_settings,name='mysettings'),

   #path('',views.index ,name='home'),
   path('maker-register/',views.maker_register ,name='maker'),

   path('checker-register/',views.checker_register ,name='checker'),

   path('login-success/',views.login_success,name='login-success'),


   path('signin/',views.custom_login,name='signin'),
#   path('login/',LoginView.as_view(template_name='users/login.html'),name='login'),
   
   
]


#redirect_authenticated_user=True
# path('profile/',views.profile,name='profile'),
# path('staff/',views.staff,name='staff'),
# path('normal/',views.normal,name='normal'),
# path('success/',views.login_success,name='success'),
