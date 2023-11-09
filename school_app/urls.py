from . import views
from django.urls import path
urlpatterns=[
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('profile',views.profile,name='profile'),
    # path('form',views.form,name='form'),
    path('form', views.show_form, name='form'),
    path('submit/', views.submit_form, name='submit')
]